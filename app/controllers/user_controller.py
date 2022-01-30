from fastapi import APIRouter
from app.config.security import get_password_hash
from app.models.requests.user_update_request import UserCreateRequest
from app.models.responses.user_response import UserResponse
from app.models.user import User
from app.controllers.decorators.create_controller import create_controller

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def add_user(createRequest: UserCreateRequest):
    properties = createRequest.dict()
    if properties['password'] is None:
        raise ValueError('User password most not be empty!')
    properties['hash_password'] = get_password_hash(properties['password'])
    del properties['password']
    entity = User(**properties)
    await entity.save()
    return entity
