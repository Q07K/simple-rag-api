from pydantic import BaseModel, ConfigDict


class Message(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    role: str
    content: str


class Messages(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    messages: list[Message] | list[None]


def set_history(messages: list[dict]):
    history = Messages(messages=messages).model_dump()
    return history.get("messages", [])
