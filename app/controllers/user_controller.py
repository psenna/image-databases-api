from typing import List

from fastapi import APIRouter
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.models.requests.user_create_request import UserCreateRequest
from app.models.requests.user_update_request import UserUpdateRequest
from app.models.responses.user_response import UserResponse
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def add_user(createRequest: UserCreateRequest):
    properties = createRequest.dict()
    properties['hash_password'] = createRequest.hash_password
    del properties['password']
    entity = User(**properties)
    await entity.save()
    return entity

@router.get("/", response_model=List[UserResponse])
@get_all_controller(User)
async def get_all_users(page: int = 1, page_size: int = 20):
    pass

@router.get("/{id}", response_model=UserResponse)
@get_one_controller(User)
async def get_user(id: int):    
    pass

@router.patch("/{id}")
@patch_controller(User)
async def patch_user(update_request: UserUpdateRequest, id: int):
    pass

@router.delete("/{id}")
@delete_controller(User)
async def delete_user(id: int):
    pass
