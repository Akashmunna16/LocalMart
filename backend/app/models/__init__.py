"""
Import all SQLAlchemy models here.

This ensures Alembic can discover them for autogeneration.
"""
from app.models.base_model import BaseModel

__all__ = [
    "BaseModel",
]