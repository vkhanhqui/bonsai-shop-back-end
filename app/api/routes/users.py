from typing import List
from fastapi import (
    APIRouter,
    status,
)

from app.services.users import UserService
from app.models.schemas import users as _uschemas


router = APIRouter()
user_service = UserService()


@router.post(
    "/sign-up",
    status_code=status.HTTP_201_CREATED,
    response_model=_uschemas.UserSignUpIn
)
async def sign_up(
    user_in: _uschemas.UserSignUpIn
):
    return user_service.sign_up(user_in)


@router.get(
    '/get-users',
    response_model=List[_uschemas.UserSignUpIn],
    status_code=status.HTTP_200_OK
)
async def get_all_users():
    return user_service.get_all_users()
