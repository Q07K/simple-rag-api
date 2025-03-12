"""chat messages model(entity)"""

import uuid

from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.postgresql import Base


# pylint:disable=not-callable, too-few-public-methods
class ChatMessageModel(Base):
    """database chat Messages Model(Entity)"""

    __tablename__ = "chat_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chat_id = Column(
        UUID(as_uuid=True),
        ForeignKey(column="chats.id", ondelete="CASCADE"),
        nullable=False,
    )
    query = Column(String, nullable=False)
    response = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    chat = relationship(argument="ChatModel", back_populates="chat_messages")
