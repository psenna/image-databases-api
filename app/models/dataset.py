from enum import unique
import ormar
from pydantic import ValidationError
from app.config.database import metadata, database

class Dataset(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "datasets"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(min_length=5, max_length=255, unique=True)


@ormar.pre_delete(Dataset)
async def dataset_has_images(sender, instance: Dataset, **kwargs):
    has_images = await instance.images.exists()
    if has_images:
        raise ValueError('A dataset with images can\'t be deleted!') 