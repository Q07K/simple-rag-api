from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from app.database.postgresql import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    load_dotenv()

    yield

    # Shutdown event
    engine.dispose()
