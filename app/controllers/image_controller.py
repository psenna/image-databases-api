from fastapi import APIRouter, Depends, HTTPException
import ormar
from app.controllers.decorators.data_is_not_valid_image import data_is_not_a_valid_image
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.entity_not_found import entity_not_found
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.models.filters.image_filters import ImageFilters
from app.models.image import Image
from app.models.label import Label
from app.models.requests.image_create_request import ImageCreateRequest
from app.models.responses.image_full_response import ImageFullResponse
from app.models.responses.image_page import ImagePage
from app.models.responses.image_slim_response import ImageSlimResponse

from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=ImageSlimResponse)
@data_is_not_a_valid_image
async def add_image(
        create_request: ImageCreateRequest,
        current_user: User = Depends(user_dependencie.get_current_user)
    ):
    dict = create_request.dict()
    dict['thumbnail'] = create_request.thumbnail
    new_image = Image(**dict)
    await new_image.save()
    return new_image

@router.get("/", response_model=ImagePage)
async def get_all_images(
    current_user: User = Depends(user_dependencie.get_current_user),
    page: int = 1, page_size: int = 20, filters: ImageFilters = Depends()):
    query = Image.objects.exclude_fields(['data'])
    if filters.dataset_name:
        query = query.filter(dataset__name=filters.dataset_name)
    if filters.label_name:
        query = query.filter(labels__name=filters.label_name)
    query = query.paginate(page=page, page_size=page_size)
    total = await query.count()
    return {
        "items": await query.all(),
        "total": total,
        "page_size": page_size,
        "page": page
        }



@router.get("/{id}", response_model=ImageFullResponse)
@get_one_controller(Image, select_all=True)
async def get_one_image(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):    
    pass

@router.delete("/{id}")
@delete_controller(Image)
async def delete_image(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    pass

@router.post("/{image_id}/labels/{label_id}", response_model=ImageSlimResponse)
async def add_label_image(
    image_id: int,
    label_id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
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
async def add_label_image(
    image_id: int,
    label_id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
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