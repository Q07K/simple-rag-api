"""token service module"""

from sqlalchemy.orm import Session

from app.config.auth.auth_jwt import create_token
from app.crud.sessions_crud import create_session, delete_session_by_user_id
from app.models.user_model import UserModel


def create_tokens(db: Session, model: UserModel) -> tuple[str, str]:
    """access, refresh token 생성 및 DB Add

    Parameters
    ----------
    db : Session
        Database session
    model : UserModel
        User Information

    Returns
    -------
    tuple[str, str]
        access_token, refresh_token
    """
    _, access_token = create_token(
        subject=model.id,
        token_type="access",
    )
    expires_at, refresh_token = create_token(
        subject=model.id,
        token_type="refresh",
    )
    delete_session_by_user_id(db=db, user_id=model.id)
    create_session(
        db=db,
        user_id=model.id,
        refresh_token=refresh_token,
        expires_at=expires_at,
    )

    return access_token, refresh_token
