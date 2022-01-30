from typing import List, Optional
from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

