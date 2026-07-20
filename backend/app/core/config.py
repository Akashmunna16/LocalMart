from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ==========================================
    # Application
    # ==========================================
    APP_NAME: str = "LocalMart API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1"

    # ==========================================
    # Database
    # ==========================================
    DATABASE_URL: str

    # ==========================================
    # Redis
    # ==========================================
    REDIS_URL: str

    # ==========================================
    # Security
    # ==========================================
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ==========================================
    # CORS
    # ==========================================
    BACKEND_CORS_ORIGINS: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()