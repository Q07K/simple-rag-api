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

# SMTP
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# WEB
WEB_URL = os.getenv("WEB_URL", "")
