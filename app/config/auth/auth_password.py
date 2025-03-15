from app.config import env
from app.config.auth.auth_jwt import pwd_context


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
