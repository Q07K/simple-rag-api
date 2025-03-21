from fastapi import FastAPI, HTTPException

from app.routers import admin_router, auth_router, chat_router
from app.routers.lifespan import lifespan
from app.services import custom_exception_response

app = FastAPI(lifespan=lifespan)

# Exception Handler
app.add_exception_handler(
    exc_class_or_status_code=HTTPException,
    handler=custom_exception_response.custom_exception_response,
)

# Include Router
app.include_router(router=admin_router.router)
app.include_router(router=auth_router.router)
app.include_router(router=chat_router.router)
