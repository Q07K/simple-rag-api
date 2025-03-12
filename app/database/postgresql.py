"""PostgreSQL connect module"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import env

SQLALCHEMY_DATABASE_URL = env.DATABASE_URL

engine = create_async_engine(url=SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase): ...


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
