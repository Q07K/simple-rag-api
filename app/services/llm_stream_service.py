import json

from sqlalchemy.orm import Session

from app.crud.chat_messages_crud import create_message
from app.crud.chats_crud import create_chat
from app.schemas.base_response import BaseResponse


def stream_response_initiate(
    db: Session,
    user_id: str,
    query: str,
    response,
):
    message_chunk = ""
    for chunk in response:
        chunk_content = chunk.choices[0].delta.content
        message_chunk += chunk_content

        yield json.dumps(
            {"message": chunk_content},
            ensure_ascii=False,
        ) + "\n"
    with db:
        chat_model = create_chat(db=db, user_id=user_id, name=query)
        create_message(
            db=db,
            chat_id=chat_model.id,
            query=query,
            response=message_chunk,
        )

    yield BaseResponse(
        status=200,
        message="create message successful",
        data={"chat_id": chat_model.id},
    ).model_dump_json()


def stream_response(
    db: Session,
    chat_id: str,
    query: str,
    response,
):
    message_chunk = ""
    for chunk in response:
        chunk_content = chunk.choices[0].delta.content
        message_chunk += chunk_content

        yield json.dumps(
            {"message": chunk_content},
            ensure_ascii=False,
        ) + "\n"

    with db:
        create_message(
            db=db,
            chat_id=chat_id,
            query=query,
            response=message_chunk,
        )
