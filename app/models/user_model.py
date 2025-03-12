"""users model(entity)"""

import uuid

from sqlalchemy import Column, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.postgresql import Base


# pylint:disable=not-callable, too-few-public-methods
class UserModel(Base):
    """database users Model(Entity)"""

    __tablename__ = "users"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    email = Column(String(length=255), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    chats = relationship(
        "ChatModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    sessions = relationship(
        "SessionModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )
