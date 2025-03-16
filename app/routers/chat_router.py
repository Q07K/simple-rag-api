from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.config.auth.auth_jwt import get_current_user
from app.crud.chat_messages_crud import get_message_by_chat_id
from app.crud.chats_crud import delete_chat_by_chat_id, get_chats_by_user_id
from app.database.postgresql import get_db
from app.schemas.base_response import BaseResponse
from app.schemas.chat_request import ChatInitiateRequest, ChatRequest
from app.schemas.chats_response import ChatResponse, ChatsResponse
from app.services.llm_stream_service import (
    stream_response,
    stream_response_initiate,
)
from app.services.rag_module.llm import tulu3_8b
from app.services.rag_module.prompt import Message, Messages

router = APIRouter(
    prefix="/v1/chats",
    tags=["Chats"],
)


@router.get("")
async def get_chats(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):
    with db:
        models = get_chats_by_user_id(db=db, user_id=user_id)
    return BaseResponse(
        status=200,
        message="Get chats successful",
        data=ChatsResponse(
            chats=[ChatResponse(**model.__dict__) for model in models]
        ),
    )


@router.get("{chat_id}")
async def get_chat_messages(
    chat_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    with db:
        models = get_message_by_chat_id(db=db, chat_id=chat_id)
    result = []
    for model in models:
        result.append(Message(role="user", content=model.query))
        result.append(Message(role="assistant", content=model.response))

    return BaseResponse(
        status=200,
        message="Get chat messages successful",
        data=Messages(messages=result),
    )


@router.post(path="/initiate")
async def initiate(
    body: ChatInitiateRequest,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
) -> StreamingResponse:
    messages = [{"role": "user", "content": body.query}]

    response = tulu3_8b(
        max_tokens=body.max_tokens,
        temperature=body.temperature,
        messages=messages,
    )

    return StreamingResponse(
        content=stream_response_initiate(
            db=db,
            user_id=user_id,
            query=body.query,
            response=response,
        ),
        media_type="text/event-stream",
    )


@router.post(path="{chat_id}/generate")
async def generate(
    chat_id: str,
    body: ChatRequest,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
) -> StreamingResponse:
    messages = list(body.messages)
    messages.append({"role": "user", "content": body.query})

    response = tulu3_8b(
        max_tokens=body.max_tokens,
        temperature=body.temperature,
        messages=messages,
    )

    return StreamingResponse(
        content=stream_response(
            db=db,
            chat_id=chat_id,
            query=body.query,
            response=response,
        ),
        media_type="text/event-stream",
    )


@router.delete("{chat_id}")
async def delete_chat(
    chat_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
) -> BaseResponse:
    with db:
        chat_id = delete_chat_by_chat_id(db=db, chat_id=chat_id)

    if chat_id is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    return BaseResponse(
        status=204,
        message="Chat deleted successfully",
        data=None,
    )
