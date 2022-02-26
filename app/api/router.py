from fastapi import APIRouter

from app.api.routes import (
    admins as admin_api,
    roles as role_api,
    products as product_api,
    customers as customer_api,
    # users as users_api,
    categories as category_api,
    files as file_api,
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


router.include_router(
    admin_api.router,
    tags=['admins'],
    prefix='/admins'
)


router.include_router(
    customer_api.router,
    tags=['customers'],
    prefix='/customers'
)


router.include_router(
    category_api.router,
    tags=['categories'],
    prefix='/categories'
)


router.include_router(
    file_api.router,
    tags=['files'],
    prefix='/files'
)
