from fastapi import APIRouter, Depends, HTTPException
import ormar
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.require_regular_user import require_regular_user
from app.models.filters.image_filters import ImageFilters
from app.models.image import Image
from app.models.label import Label
from app.models.schemes.image_schemes import ImageFullResponse, ImagePage, ImageSlimResponse, ImageCreateRequest
from app.models.schemes.pagination_scheme import PaginationParameters

from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=ImageSlimResponse, )
@require_regular_user
@create_controller(Image)
async def add_image(create_request: ImageCreateRequest):
    """
    Create a image.
    """

@router.get("/", response_model=ImagePage)
@require_regular_user
@get_all_controller(Image)
async def get_all_images(
    pagination_parameters: PaginationParameters = Depends(),
    filters: ImageFilters = Depends()):
    """
    Get images with pagination and filters.
    The image data is not returned in this request.
    """


@router.get("/{id}", response_model=ImageFullResponse)
@require_regular_user
@get_one_controller(Image, select_all=True)
async def get_one_image(id: int):    
    """
    Get a image by id with image data.
    """

@router.delete("/{id}")
@require_regular_user
@delete_controller(Image)
async def delete_image(id: int):
    """
    Delete a image.
    """

@router.post("/{image_id}/labels/{label_id}", response_model=ImageSlimResponse)
@require_regular_user
async def add_label_image(image_id: int, label_id: int):
    """
    Add a label to a image.
    """
    try:
        image = await Image.objects.exclude_fields('data').select_all().get(id=image_id)
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Image not found!")
    try:
        label = await Label.objects.get(id=label_id)
    except ormar.exceptions.NoMatch:    
        raise HTTPException(status_code=404, detail="Label not found!")
    await image.labels.add(label)
    return image
    

@router.delete("/{image_id}/labels/{label_id}", response_model=ImageSlimResponse)
@require_regular_user
async def add_label_image(image_id: int, label_id: int):
    """
    Remove a label from a image.
    """
    try:
        image = await Image.objects.exclude_fields('data').select_all().get(id=image_id)
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Image not found!")
    try:
        label = await Label.objects.get(id=label_id)
    except ormar.exceptions.NoMatch:    
        raise HTTPException(status_code=404, detail="Label not found!")
    await image.labels.remove(label)
    return image