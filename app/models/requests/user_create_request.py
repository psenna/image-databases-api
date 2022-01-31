from pydantic import BaseModel
from app.config.security import get_password_hash

class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str
    
    class Config:
        exclude = {'password'}

    @property
    def hash_password(self) -> str:
        return get_password_hash(self.password)
