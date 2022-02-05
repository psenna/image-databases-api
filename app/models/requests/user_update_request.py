from typing import Optional
from pydantic import BaseModel, Field, validator
from app.config.security import get_password_hash

class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    hash_password: Optional[str] = Field(alias='password', default=None)

    @validator('hash_password')
    def hash_the_password(cls, v):
        return get_password_hash(v)