from uuid import UUID

from pydantic import BaseModel


class ChatResponse(BaseModel):
    id: UUID
    name: str


class ChatsResponse(BaseModel):
    chats: list[ChatResponse] | list[None]
