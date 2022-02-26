# from typing import List
# from fastapi import (
#     APIRouter,
#     status,
# )

# from app.services.users import UserService
# from app.models.schemas import (
#     users as _user_schemas,
# )

# router = APIRouter()
# user_service = UserService()


# @router.post(
#     "/create_user",
#     status_code=status.HTTP_201_CREATED,
#     response_model=_user_schemas.UserResDetail
# )
# async def create_user(user_in: _user_schemas.UserInCreate):
#     return user_service.create_user(user_in)


# @router.get(
#     "/get-all-users",
#     status_code=status.HTTP_200_OK,
#     response_model=List[_user_schemas.UserResDetail],
# )
# async def get_all_users():
#     return user_service.get_all_users()


# @router.get(
#     "/{user_id}",
#     status_code=status.HTTP_200_OK,
#     response_model=_user_schemas.UserResDetail
# )
# async def get_user_by_id(user_id: int):
#     return user_service.get_user_by_id(user_id)
