from datetime import datetime, timedelta, timezone
from typing import Literal

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext

from app.config import env

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_token(
    subject: str,
    expires_delta: timedelta | None = None,
    token_type: Literal["access", "refresh"] = "access",
) -> tuple[datetime, str]:
    """Create Json Web Token

    Parameters
    ----------
    subject : str
        user ID
    expires_delta : timedelta | None, optional
        Token 유효기간, by default None
    token_type : Literal["access", "refresh"], optional
        Token type, by default "access"

    Returns
    -------
    str
        Json Web Token
    """

    expire = datetime.now(timezone.utc)

    match token_type:
        case "access":
            expires_delta = timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)
        case "refresh":
            expires_delta = timedelta(minutes=env.REFRESH_TOKEN_EXPIRE_MINUTES)

    expire += expires_delta

    to_encode = {
        "exp": expire,
        "sub": str(subject),
        "type": token_type,
    }

    return expire, jwt.encode(
        claims=to_encode,
        key=env.SECRET_KEY,
        algorithm=env.ALGORITHM,
    )
