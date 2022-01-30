from fastapi import APIRouter

router = APIRouter()

from app.controllers.user_controller import router as user_router

router.include_router(user_router, prefix='/users', tags=['User'])