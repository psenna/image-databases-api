import ormar
from functools import wraps
from pydantic import BaseModel

from app.models.user import User

def create_controller (model: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper(create_request: BaseModel, current_user: User = None):
            properties = create_request.dict(exclude_unset=True)
            entity = model(**properties)
            await entity.save()
            return entity
        return wrapper
    return inner