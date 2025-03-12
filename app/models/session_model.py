"""sessions model(entity)"""

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.postgresql import Base


# pylint:disable=not-callable, too-few-public-methods
class SessionModel(Base):
    """database sessions Model(Entity)"""

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey(column="users.id", ondelete="CASCADE"),
        nullable=False,
    )
    refresh_token = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP, default=func.now())
    expires_at = Column(TIMESTAMP, nullable=False)

    user = relationship(argument="UserModel", back_populates="sessions")
