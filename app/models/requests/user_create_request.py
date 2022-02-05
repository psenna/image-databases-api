from pydantic import BaseModel, Field, validator

from app.config.security import get_password_hash

class UserCreateRequest(BaseModel):
    name: str
    email: str
    hash_password: str = Field(alias='password')

    @validator('hash_password')
    def hash_the_password(cls, v):
        return get_password_hash(v)
