from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.exceptions import LocalMartException
from app.schemas.responses import ErrorItem, ErrorResponse


async def localmart_exception_handler(
    request: Request,
    exc: LocalMartException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            success=False,
            message=exc.detail,
            errors=None,
        ).model_dump(),
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    errors = []

    for error in exc.errors():
        errors.append(
            ErrorItem(
                field=".".join(map(str, error["loc"])),
                detail=error["msg"],
            )
        )

    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            success=False,
            message="Validation failed",
            errors=errors,
        ).model_dump(),
    )


async def general_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            success=False,
            message="Internal server error",
            errors=None,
        ).model_dump(),
    )
