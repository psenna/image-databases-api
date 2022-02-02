from fastapi import APIRouter, Depends, HTTPException
import ormar
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.entity_not_found import entity_not_found
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.models.image import Image
from app.models.label import Label
from app.models.requests.image_create_request import ImageCreateRequest
from app.models.responses.image_full_response import ImageFullResponse
from app.models.responses.image_slim_response import ImageSlimResponse
from app.models.responses.page import Page

from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=ImageSlimResponse)
async def add_image(
        create_request: ImageCreateRequest,
        current_user: User = Depends(user_dependencie.get_current_user)
    ):
    dict = create_request.dict()
    dict['thumbnail'] = create_request.thumbnail
    new_image = Image(**dict)
    await new_image.save()
    return new_image

@router.get("/", response_model=Page[ImageSlimResponse])
@get_all_controller(Image, exclude_fields=['data'])
async def get_all_images(
    current_user: User = Depends(user_dependencie.get_current_user),
    page: int = 1, page_size: int = 20):
    pass

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