from typing import List
from fastapi import (
    APIRouter,
    status,
    Depends,
)

from app.services.ratings import RatingService
from app.models.domains import (
    base as _base_domains
)
from app.models.schemas import (
    ratings as _ratings_schemas,
    auth as _auth_schemas,
)
from app.utils import auth_utils as _auth_utils


router = APIRouter()
rating_service = RatingService()


@router.post(
    "/create-rating",
    status_code=status.HTTP_201_CREATED,
    response_model=_base_domains.Message
)
async def create_rating(
    rating_in: _ratings_schemas.RatingInCreate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return rating_service.create_rating(current_user, rating_in)


@router.get(
    '/get-all-ratings/{product_id}',
    response_model=List[_ratings_schemas.RatingRespDetail],
    status_code=status.HTTP_200_OK
)
async def get_all_ratings(product_id: int):
    return rating_service.get_all_ratings(product_id)


@router.put(
    "/update-rating-as-customer",
    status_code=status.HTTP_200_OK,
    response_model=_ratings_schemas.RatingCustomerInUpdate
)
async def update_rating_as_customer(
    rating_in: _ratings_schemas.RatingCustomerInUpdate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return rating_service.update_rating_as_customer(current_user, rating_in)


@router.put(
    "/update-rating-as-staff",
    status_code=status.HTTP_200_OK,
    response_model=_ratings_schemas.RatingStaffInUpdate
)
async def update_rating_as_staff(
    rating_in: _ratings_schemas.RatingStaffInUpdate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return rating_service.update_rating_as_staff(current_user, rating_in)


@router.delete(
    "/delete-rating/{rating_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domains.Message
)
async def delete_rating(
    rating_id: int,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return rating_service.delete_rating(current_user, rating_id)
