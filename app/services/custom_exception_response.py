from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from app.schemas.base_response import BaseResponse


async def custom_exception_response(
    _: Request,
    exc: HTTPException,
) -> JSONResponse:
    """Exception handling function

    Parameters
    ----------
    _ : Request
        Request object
    exc : HTTPException
        Raised HTTP Exception

    Returns
    -------
    JSONResponse
        Custom 응답 형식
    """
    status_code = exc.status_code
    if exc.status_code == 401:
        if exc.detail.lower().endswith("token expired"):
            status_code = 40101

    response = BaseResponse(
        status=status_code,
        message=exc.detail,
        data=None,
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(),
    )
