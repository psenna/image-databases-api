import ormar
from app.config.database import metadata, database

class Dataset(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "datasets"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255)