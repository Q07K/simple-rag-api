from sqlalchemy import select
from sqlalchemy.orm import Session

# pylint:disable=wildcard-import, unused-wildcard-import
from app.models import *
from app.models import UserModel


def create_user(
    db: Session,
    email: str,
    hashed_password: str,
):
    model = UserModel(email=email, hashed_passwor=hashed_password)
    db.add(model)
    db.commit()


def get_user_by_email(
    db: Session,
    email: str,
) -> UserModel:
    return db.execute(
        statement=select(UserModel).where(UserModel.email == email)
    ).scalar_one()
