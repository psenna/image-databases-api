import ormar
from functools import wraps
from pydantic import BaseModel

from app.models.user import User

def create_controller (model: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper(current_user: User, createRequest: BaseModel):
            properties = createRequest.dict()
            print(properties)
            entity = model(**properties)
            await entity.save()
            return entity
        return wrapper
    return inner