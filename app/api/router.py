from fastapi import APIRouter

from app.api.routes import (
    roles as role_api,
    products as product_api,
)


router = APIRouter()


router.include_router(
    product_api.router,
    tags=['products'],
    prefix='/products'
)

router.include_router(
    role_api.router,
    tags=['roles'],
    prefix='/roles'
)
