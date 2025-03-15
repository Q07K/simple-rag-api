from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config.auth.auth_password import verify_password
from app.crud.users_crud import get_user_by_email
from app.database.postgresql import get_db
from app.schemas.base_response import BaseResponse
from app.services.token_service import create_tokens

router = APIRouter(
    prefix="/v1/auth",
    tags=["Auth"],
)


@router.post(path="/login")
async def login(
    response: Response,
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> BaseResponse:
    """
    ## User Login
    - **email**: User's email (used as the username in OAuth2 form)
    - **password**: User's password

    **Returns:**
    - `200`: Login successful, returns access & refresh tokens.
    - `401`: Invalid email or password.
    """
    with db:
        model = get_user_by_email(db=db, email=form_data.username)

        is_verify_password = verify_password(
            plain_password=form_data.password,
            hashed_password=model.hashed_password,
        )

        if not is_verify_password:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )

        access_token, refresh_token = create_tokens(db, model)

    response_dict = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer",
    }
    for response_key, response_value in response_dict.items():
        response.set_cookie(
            key=response_key,
            value=response_value,
            httponly=True,
            samesite="Strict",
        )

    return BaseResponse(status=200, message="Login successful")
