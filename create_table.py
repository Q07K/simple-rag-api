from dotenv import load_dotenv

from app.database.postgresql import Base, engine
from app.models import (
    chat_message_model,
    chat_model,
    session_model,
    user_model,
)


def create_table():
    load_dotenv()

    chat_model.ChatModel
    chat_message_model.ChatMessageModel
    session_model.SessionModel
    user_model.UserModel

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_table()
