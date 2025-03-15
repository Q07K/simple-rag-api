import random
import string

from app.config import env
from app.config.auth.auth_jwt import pwd_context


def generate_password(length=12) -> str:
    """password 생성

    Parameters
    ----------
    length : int, optional
        password 생성 길이이, by default 12

    Returns
    -------
    str
        password
    """
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # 비밀번호 생성
    return "".join(random.choice(all_characters) for _ in range(length))


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
    return pwd_context.hash(password + env.SECRET_SALT)


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
    return pwd_context.verify(
        plain_password + env.SECRET_SALT,
        hashed_password,
    )
