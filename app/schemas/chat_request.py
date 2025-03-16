from app.services.rag_module.prompt import Messages


class ChatRequest(Messages):
    query: str
