import ormar
from app.config.database import metadata, database

class Image(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255)
    data: str = ormar.LargeBinary(
        max_length=100000, represent_as_base64_str=True
    )