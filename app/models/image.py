from enum import unique
import ormar
from app.config.database import metadata, database
from app.models.dataset import Dataset
from app.models.label import Label

class Image(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "images"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255, unique=True)
    data: str = ormar.LargeBinary(
        max_length=100000, represent_as_base64_str=False, nullable=True 
    )
    thumbnail: str = ormar.LargeBinary(
        max_length=100000, represent_as_base64_str=False, nullable=True
    )
    dataset: Dataset = ormar.ForeignKey(
        Dataset,
        ondelete='restrict',
        onupdate='restrict'
    )
    labels = ormar.ManyToMany(Label,
        through_relation_name="image_id",
        through_reverse_relation_name="label_id")
