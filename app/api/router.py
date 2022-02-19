from fastapi import APIRouter

from app.api.routes import (
    users as user_api,
)


router = APIRouter()

router.include_router(
    user_api.router,
    tags=['users'],
    prefix='/users'
)
