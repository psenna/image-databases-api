import ormar
from functools import wraps
from pydantic import BaseModel

def create_controller (model: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper(createRequest: BaseModel):
            properties = createRequest.dict()
            print(properties)
            entity = model(**properties)
            await entity.save()
            return entity
        return wrapper
    return inner