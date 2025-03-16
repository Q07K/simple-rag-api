from datetime import timedelta

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

# pylint:disable=wildcard-import, unused-wildcard-import
from app.models import *
from app.models.session_model import SessionModel


def create_session(
    db: Session,
    user_id: str,
    refresh_token: str,
    expires_at: timedelta,
) -> None:
    model = SessionModel(
        user_id=user_id,
        refresh_token=refresh_token,
        expires_at=expires_at,
    )
    db.add(model)
    db.commit()


def get_session_by_user_id(
    db: Session,
    user_id: str,
) -> SessionModel | None:
    stmp = select(SessionModel).where(SessionModel, user_id == user_id)
    return db.execute(stmp).scalar_one_or_none()


def delete_session_by_user_id(
    db: Session,
    user_id: str,
):
    smtp = delete(SessionModel).where(SessionModel.user_id == user_id)
    result = db.execute(statement=smtp)
    db.commit()

    return result.rowcount
