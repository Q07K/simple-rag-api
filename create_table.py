from dotenv import load_dotenv

from app.database.postgresql import Base, engine
from app.models import *


def create_table():
    load_dotenv()

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_table()
