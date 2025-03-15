from fastapi import FastAPI, HTTPException

from app.routers import admin_router, auth_router
from app.services import custom_exception_response

app = FastAPI()

# Exception Handler
app.add_exception_handler(
    exc_class_or_status_code=HTTPException,
    handler=custom_exception_response.custom_exception_response,
)

# Include Router
app.include_router(router=admin_router.router)
app.include_router(router=auth_router.router)
