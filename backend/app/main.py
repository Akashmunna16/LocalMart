from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.core.exception_handlers import (
    general_exception_handler,
    localmart_exception_handler,
    validation_exception_handler,
)
from app.core.lifespan import lifespan
from app.exceptions import LocalMartException

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
## LocalMart API

AI-powered hyperlocal e-commerce platform connecting
local vendors with nearby customers.

### Features

- Customer Marketplace
- Vendor Dashboard
- Order Management
- AI Recommendations
- Payments
- Analytics

Built using FastAPI.
""",
    contact={
        "name": "LocalMart Team",
        "email": "support@localmart.dev",
    },
    license_info={
        "name": "MIT",
    },
    lifespan=lifespan,
    exception_handlers={
        LocalMartException: localmart_exception_handler,
        RequestValidationError: validation_exception_handler,
        Exception: general_exception_handler,
    },
)

app.add_exception_handler(
    LocalMartException,
    localmart_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    general_exception_handler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/")
def root():
    return {"message": "Welcome to LocalMart API"}
