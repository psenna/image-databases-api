from email.policy import default
import ormar
import re
from pydantic import validator

from app.config.database import metadata, database

class User(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    hash_password: str = ormar.String(max_length=255)
    is_superuser: bool = ormar.Boolean(default=False)

    @validator('email')
    def valida_formatacao_sigla(cls, v):
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(v):
            raise ValueError('The user email format is invalid!')
        return v