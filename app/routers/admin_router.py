from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config import env
from app.config.auth.auth_password import generate_password, get_password_hash
from app.crud.users_crud import create_user, get_user_by_email
from app.database.postgresql import get_db
from app.schemas.base_response import BaseResponse
from app.schemas.token_request import AdminToken
from app.services.smtp import send_invite_email

router = APIRouter(
    prefix="/v1/admin",
    tags=["Admin"],
)


@router.post(path="/invite")
async def invite(
    body: AdminToken,
    db: Session = Depends(get_db),
) -> BaseResponse:
    """
    ## Invite a New User

    This endpoint allows administrators or authorized users to invite a new user.
    The following steps occur when this endpoint is called:

    - **Generates a random initial password** for the user.
    - **Hashes the password** for secure storage.
    - **Creates the user** in the database.
    - **Sends an invitation email** to the user with the password.

    ### Responses:
    - **200**: Successfully invited the user and sent an email.
    - **401**: Invalid password.
    - **400**: If the input data is invalid, like missing or incorrect fields.
    """
    if body.token != env.SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid password")

    with db:
        if get_user_by_email(db=db, email=body.email):
            raise HTTPException(status_code=409, detail="User already exists")

        init_password = generate_password()
        hashed_password = get_password_hash(password=init_password)
        create_user(db=db, email=body.email, hashed_password=hashed_password)

    message = send_invite_email(
        name=body.name,
        email=body.email,
        password=init_password,
    )
    return BaseResponse(status=200, message=message)
