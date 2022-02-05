import secrets

from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ImageDatasetApi"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URL: str = "sqlite:///db.sqlite"
    TEST_DATABASE: bool = False
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24
    THUMBNAIL_SIZE: int = 36
    ADMIN_PASSWORD: str = "admin"
    PASSWORD_HASH_ALGORITHM: str = "sha256_crypt"
    JWT_ALGORITHM: str = "HS512"

    class Config:
        env_file = ".env"

settings = Settings()