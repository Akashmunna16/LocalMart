from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting LocalMart API...")

    # Future startup tasks:
    # - Connect PostgreSQL
    # - Connect Redis
    # - Load AI models
    # - Initialize scheduler

    yield

    logger.info("🛑 Shutting down LocalMart API...")

    # Future shutdown tasks:
    # - Close DB connections
    # - Close Redis
    # - Stop background workers
