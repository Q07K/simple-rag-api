from app.schemas.user_request import UserRequest


class AdminToken(UserRequest):
    token: str
