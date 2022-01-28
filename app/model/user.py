import ormar
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