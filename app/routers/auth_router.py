from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config.auth.security import verify_password
from app.crud.users_crud import get_user_by_email
from app.database.postgresql import get_db
from app.schemas.base_response import BaseResponse
from app.schemas.security_schema import TokenModel
from app.services.token_service import create_tokens

router = APIRouter(
    prefix="/v1/auth",
    tags=["Auth"],
)


@router.post(path="/login")
async def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> BaseResponse:
    """
    ## User Login API
    - **email**: User's email (used as the username in OAuth2 form)
    - **password**: User's password

    **Returns:**
    - `200`: Login successful, returns access & refresh tokens.
    - `401`: Invalid email or password.
    """
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

    return BaseResponse(
        status=200,
        message="Login successful",
        data=TokenModel(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
        ),
    )
