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
) -> str:
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

    if expires_delta is None:
        expires_delta = timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)

    expire += expires_delta

    to_encode = {
        "exp": expire,
        "sub": str(subject),
        "type": token_type,
    }

    return jwt.encode(
        claims=to_encode,
        key=env.SECRET_KEY,
        algorithm=env.ALGORITHM,
    )


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """password 검증

    Parameters
    ----------
    plain_password : str
        password
    hashed_password : str
        암호화된 password

    Returns
    -------
    bool
        password 검증 결과
        - True: 검증 성공
        - False: 검증 실패
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """password 암호화

    Parameters
    ----------
    password : str
        password

    Returns
    -------
    str
        암호화된 password
    """
    return pwd_context.hash(password)
