"""PostgreSQL connect module"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from app.config import env


SQLALCHEMY_DATABASE_URL = env.DATABASE_URL

engine = create_async_engine(url=SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()


async def get_db():
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
        await db.close()
