from typing import List
from fastapi import (
    APIRouter,
    status,
    Depends,
)

from app.services.categories import CategoryService
from app.models.domains import (
    base as _base_domains
)
from app.models.schemas import (
    categories as _category_schemas,
    auth as _auth_schemas,
)
from app.utils import auth_utils as _auth_utils


router = APIRouter()
category_service = CategoryService()


@router.post(
    "/create-category",
    status_code=status.HTTP_201_CREATED,
    response_model=_category_schemas.CategoryRespDetail
)
async def create_category(
    category_in: _category_schemas.CategoryInCreate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return category_service.create_category(current_user, category_in)


@router.get(
    '/get-all-categories',
    response_model=List[_category_schemas.CategoryRespDetail],
    status_code=status.HTTP_200_OK
)
async def get_all_categories():
    return category_service.get_all_categories()


@router.put(
    "/update-category",
    status_code=status.HTTP_200_OK,
    response_model=_category_schemas.CategoryInUpdate
)
async def update_category(
    category_in: _category_schemas.CategoryInUpdate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return category_service.update_category(current_user, category_in)


@router.delete(
    "/delete-category/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domains.Message
)
async def delete_category(
    category_id: int,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return category_service.delete_category(current_user, category_id)
