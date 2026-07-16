from fastapi import APIRouter

from app.core.config import settings
from app.schemas.responses import ApiResponse

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=ApiResponse,
)
def health():

    return ApiResponse(
        success=True,
        message="Health check successful",
        data={
            "status": "healthy",
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
        },
    )
