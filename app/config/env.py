import os

# PostgreSQL Client
DATABASE_URL = (
    "postgresql://"
    + os.getenv(key="POSTGRESQL_ID", default="postgres")
    + ":"
    + os.getenv(key="POSTGRESQL_PW", default="")
    + "@"
    + os.getenv(key="POSTGRESQL_URL", default="localhost")
    + ":"
    + os.getenv(key="POSTGRESQL_PORT", default="5432")
    + "/"
    + os.getenv(key="POSTGRESQL_DB", default="default")
)

# Token
SECRET_KEY = os.getenv(key="SECRET_KEY", default="password")
ALGORITHM = os.getenv(key="ALGORITHM", default="default")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        key="ACCESS_TOKEN_EXPIRE_MINUTES",
        default="30",
    )
)
REFRESH_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        key="REFRESH_TOKEN_EXPIRE_MINUTES",
        default="1440",
    )
)
# SMTP
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# WEB
WEB_URL = os.getenv("WEB_URL", "")
