"""chats model(entity)"""

import uuid

from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.postgresql import Base


# pylint:disable=not-callable, too-few-public-methods
class ChatModel(Base):
    """database chat Model(Entity)"""

    __tablename__ = "chats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey(column="users.id", ondelete="CASCADE"),
        nullable=False,
    )
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    user = relationship(
        argument="UserModel",
        back_populates="chats",
    )
    chat_messages = relationship(
        argument="ChatMessageModel",
        back_populates="chat",
        cascade="all, delete-orphan",
    )
