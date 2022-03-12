from typing import List
from fastapi import (
    APIRouter,
    status,
    Depends,
)

from app.services.roles import RoleService
# from app.models.domains import (
#     base as _base_domains
# )
from app.models.schemas import (
    roles as _role_schemas,
    auth as _auth_schemas,
)
from app.utils import auth_utils as _auth_utils


router = APIRouter()
role_service = RoleService()


# @router.post(
#     "/create-role",
#     status_code=status.HTTP_201_CREATED,
#     response_model=_role_schemas.RoleRespDetail
# )
# async def create_role(
#     role_in: _role_schemas.RoleInCreate
# ):
#     return role_service.create_role(role_in)


@router.get(
    '/get-all-roles',
    response_model=List[_role_schemas.RoleRespDetail],
    status_code=status.HTTP_200_OK
)
async def get_all_roles(
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return role_service.get_all_roles(current_user)


# @router.put(
#     "/update-role",
#     status_code=status.HTTP_200_OK,
#     response_model=_role_schemas.RoleInUpdate
# )
# async def update_role(
#     role_in: _role_schemas.RoleInUpdate
# ):
#     return role_service.update_role(role_in)


# @router.delete(
#     "/delete-role/{role_id}",
#     status_code=status.HTTP_200_OK,
#     response_model=_base_domains.Message
# )
# async def delete_role(
#     role_id: int
# ):
#     return role_service.delete_role(role_id)
