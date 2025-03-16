from typing import Sequence
from uuid import UUID

from sqlalchemy import Column, select
from sqlalchemy.orm import Session

from app.models.chat_model import ChatModel


def create_chat(
    db: Session,
    user_id: str,
    name: str,
) -> ChatModel:
    model = ChatModel(name=name, user_id=user_id)
    db.add(model)
    db.commit()

    return model


def get_chats_by_user_id(
    db: Session,
    user_id: str,
) -> Sequence[ChatModel]:
    smtp = select(ChatModel).where(ChatModel.user_id == user_id)
    result = db.execute(statement=smtp)
    db.commit()

    return result.scalars().all()


def delete_chat_by_chat_id(
    db: Session,
    chat_id: str,
) -> Column[UUID] | None:
    model = db.get(ChatModel, chat_id)
    if model:
        db.delete(model)
        db.commit()

        return model.id
