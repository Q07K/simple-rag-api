from pydantic import BaseModel

from app.services.rag_module.prompt import Messages


class ChatInitiateRequest(BaseModel):
    temperature: float
    max_tokens: int
    query: str


class ChatRequest(Messages, ChatInitiateRequest): ...
