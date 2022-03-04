from fastapi import APIRouter, Depends
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.entity_not_found import entity_not_found
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.controllers.decorators.require_regular_user import require_regular_user
from app.models.dataset import Dataset
from app.models.filters.dataset_filters import DatasetFilters
from app.models.schemes.dataset_schemes import DatasetCreateRequest, DatasetUpdateRequest, DatasetResponse, DatasetPage
from app.models.schemes.pagination_scheme import PaginationParameters
from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=DatasetResponse)
@require_regular_user
@create_controller(Dataset)
async def add_dataset(create_request: DatasetCreateRequest):
    """
    Create a dataset.
    """

@router.get("/", response_model=DatasetPage)
@require_regular_user
@get_all_controller(Dataset)
async def get_all_datasets(
    pagination_parameters: PaginationParameters = Depends(),
    filters: DatasetFilters = Depends()):
    """
    List all the datasets with pagination.
    """

@router.get("/{id}", response_model=DatasetResponse)
@require_regular_user
@get_one_controller(Dataset)
async def get_one_dataset(id: int):    
    """
    Get one dataset by its id
    """

@router.patch("/{id}", response_model=DatasetResponse)
@require_regular_user
@patch_controller(Dataset)
async def patch_dataset(update_request: DatasetUpdateRequest, id: int):
    """
    Update a dataset. Only the dataset name can be updated.
    """

@router.delete("/{id}")
@require_regular_user
@delete_controller(Dataset)
async def delete_dataset(id: int):
    """
    Delete a dataset and all the images related to it.
    A dataset with images can't be deleted, clear the dataset first with DELETE /datasets/:id/images
    """

@router.delete("/{id}/images")
@require_regular_user
@entity_not_found
async def delete_all_dataset_images(id: int):
    """
    Delete all the images in a dataset.
    After this operation, the dataset can be deleted.
    """
    dataset = await Dataset.objects.select_all().get(id=id)
    await dataset.images.clear(keep_reversed=False)
    return {"message": "The dataset was clear, now it can be deleted!"}