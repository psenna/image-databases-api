import ormar
from app.config.database import metadata, database

class Label(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "labels"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255)