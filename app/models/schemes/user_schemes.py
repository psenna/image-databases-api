from typing import List, Optional
from pydantic import BaseModel, Field, validator

from app.config.security import get_password_hash

class UserCreateRequest(BaseModel):
    name: str
    email: str
    hash_password: str = Field(alias='password')

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        return get_password_hash(v)

class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    hash_password: Optional[str] = Field(alias='password', default=None)

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        return get_password_hash(v)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_superuser: bool


class UserPage(BaseModel):
    items: List[UserResponse]
    total: int
    page_size: int
    page: int