from pydantic import BaseModel


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenDataModel(BaseModel):
    user_id: str | None = None
