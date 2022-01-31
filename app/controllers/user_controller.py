from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.config.security import create_access_token, verify_password
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.models.requests.login_request import LoginRequest
from app.models.requests.user_create_request import UserCreateRequest
from app.models.requests.user_update_request import UserUpdateRequest
from app.models.responses.user_response import UserResponse
from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def add_user(
    createRequest: UserCreateRequest,
    current_user: User = Depends(user_dependencie.get_current_superuser)
    ):
    properties = createRequest.dict()
    properties['hash_password'] = createRequest.hash_password
    del properties['password']
    entity = User(**properties)
    await entity.save()
    return entity

@router.get("/", response_model=List[UserResponse])
@get_all_controller(User)
async def get_all_users(
    current_user: User = Depends(user_dependencie.get_current_superuser),
    page: int = 1, page_size: int = 20):
    pass

@router.get("/{id}", response_model=UserResponse)
@get_one_controller(User)
async def get_user(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):    
    pass

@router.patch("/{id}", response_model=UserResponse)
@patch_controller(User)
async def patch_user(
    update_request: UserUpdateRequest, id: int,
    current_user: User = Depends(user_dependencie.get_current_superuser)):
    pass

@router.delete("/{id}")
@delete_controller(User)
async def delete_user(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_superuser)):
    pass

@router.post("/login")
async def login(login_request: LoginRequest):
    user = await User.objects.get_or_none(email=login_request.email)
    if not user or not verify_password(login_request.password, user.hash_password):
        raise HTTPException(status_code=403, detail="Worng user email or password!")
    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer",
    }