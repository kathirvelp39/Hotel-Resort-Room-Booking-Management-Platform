from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "StayNest Pro - Hotel, Resort & Room Booking Management"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = ""

    # Database
    SQLALCHEMY_DATABASE_URL: str

    # Security & JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # File uploads
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE_MB: int = 10
    ALLOWED_IMAGE_EXTENSIONS: List[str] = ["jpg", "jpeg", "png", "webp"]
    ALLOWED_DOC_EXTENSIONS: List[str] = ["pdf", "jpg", "jpeg", "png", "docx"]

    # Stripe
    STRIPE_API_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""

    # External AI Providers
    OPENAI_API_KEY: str = ""
    GEMINI_API_KEY: str = ""

    # Environment
    ENVIRONMENT: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
