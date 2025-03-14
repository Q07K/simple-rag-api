from fastapi import FastAPI, HTTPException

from app.services import custom_exception_response

app = FastAPI()

app.add_exception_handler(
    HTTPException,
    custom_exception_response.custom_exception_response,
)


@app.get("/{test}")
async def root(test: str):
    if test == "test":
        raise HTTPException(
            status_code=400,
            detail="This is an error",
        )
    if test == "a":
        raise HTTPException(
            status_code=401,
            detail="access token expired",
        )
    return {"message": "Hello World"}
