from datetime import timedelta

from sqlalchemy.orm import Session

# pylint:disable=wildcard-import, unused-wildcard-import
from app.models import *


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
    db.close()
