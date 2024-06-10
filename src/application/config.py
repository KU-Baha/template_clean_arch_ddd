from datetime import datetime, timedelta

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Postgres
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    # Celery
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # Auth service
    AUTH_SERVICE_URL: str
    PROJECT_NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


class JWTSettings(BaseSettings):
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE: int
    REFRESH_TOKEN_EXPIRE: int
    ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


class CORSConfig:
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
jwt_settings = JWTSettings()
cors_config = CORSConfig()
