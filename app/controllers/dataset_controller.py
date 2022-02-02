from fastapi import APIRouter, Depends
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.models.dataset import Dataset
from app.models.requests.dataset_create_request import DatasetCreateRequest
from app.models.requests.dataset_update_request import DatasetUpdateRequest

from app.models.responses.dataset_response import DatasetResponse
from app.models.responses.page import Page
from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=DatasetResponse)
@create_controller(Dataset)
async def add_dataset(
        create_request: DatasetCreateRequest,
        current_user: User = Depends(user_dependencie.get_current_user)
    ):
    pass

@router.get("/", response_model=Page[DatasetResponse])
@get_all_controller(Dataset)
async def get_all_datasets(
    current_user: User = Depends(user_dependencie.get_current_user),
    page: int = 1, page_size: int = 20):
    pass

@router.get("/{id}", response_model=DatasetResponse)
@get_one_controller(Dataset)
async def get_one_dataset(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):    
    pass

@router.patch("/{id}", response_model=DatasetResponse)
@patch_controller(Dataset)
async def patch_dataset(
    update_request: DatasetUpdateRequest, id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    pass

@router.delete("/{id}")
@delete_controller(Dataset)
async def delete_dataset(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    pass