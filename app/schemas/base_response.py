from typing import Any

from pydantic import BaseModel, ConfigDict


class BaseResponse(BaseModel):
    """Base Response"""

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    status: int
    message: str
    data: Any | list[Any] | None = None
