import secrets

from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ImageDatabaseApi"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URI: str = "sqlite:///db.sqlite"
    TEST_DATABASE: bool = False

    class Config:
        env_file = ".env"

settings = Settings()