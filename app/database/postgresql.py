"""PostgreSQL connect module"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import env

SQLALCHEMY_DATABASE_URL = env.DATABASE_URL

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

Base = declarative_base()

# class Base(DeclarativeBase): ...


def get_db():
    """database connection session

    Yields
    ------
    session
        SQLAlchemy session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
