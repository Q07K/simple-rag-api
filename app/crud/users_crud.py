from sqlalchemy.orm import Session

# pylint:disable=wildcard-import, unused-wildcard-import
from app.models import *
from app.models import UserModel


def get_user_by_email(
    db: Session,
    email: str,
) -> UserModel:
    return db.query(UserModel).filter_by(email=email).first()
