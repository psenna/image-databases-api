from typing import List, Optional
from pydantic import BaseModel
from app.config.security import get_password_hash

class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    @property
    def hash_password(self) -> str:
        return get_password_hash(self.password)