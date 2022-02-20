from fastapi import APIRouter

from app.api.routes import (
    roles as role_api,
)


router = APIRouter()

router.include_router(
    role_api.router,
    tags=['roles'],
    prefix='/roles'
)
