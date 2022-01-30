from pydantic import BaseModel, Field
from sqlalchemy import false

from app.config.security import get_password_hash

class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str = Field(title="User password", Optional=false)
    
    class Config:
        exclude = {'password'}

    @property
    def hash_password(self) -> str:
        return get_password_hash(self.password)
