from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chat_message_model import ChatMessageModel


def create_message(
    db: Session,
    chat_id: str,
    query: str,
    response: str,
) -> None:
    model = ChatMessageModel(
        query=query,
        response=response,
        chat_id=chat_id,
    )
    db.add(model)
    db.commit()


def get_message_by_chat_id(
    db: Session,
    chat_id: str,
) -> Sequence[ChatMessageModel]:
    smtp = select(ChatMessageModel).where(ChatMessageModel.chat_id == chat_id)
    result = db.execute(statement=smtp)
    return result.scalars().all()
