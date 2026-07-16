from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None


class ErrorItem(BaseModel):
    field: str | None = None
    detail: str


class ErrorResponse(BaseModel):
    success: bool
    message: str
    errors: list[ErrorItem] | None = None
