from typing import List
from fastapi import (
    APIRouter,
    status,
)

from app.services.roles import RoleService
from app.models.domains import (
    base as _base_domain
)
from app.models.schemas import (
    roles as _role_schemas,
)


router = APIRouter()
role_service = RoleService()


@router.post(
    "/create-role",
    status_code=status.HTTP_201_CREATED,
    response_model=_role_schemas.RoleRespDetail
)
async def create_role(
    role_in: _role_schemas.RoleInCreate
):
    return role_service.create_role(role_in)


@router.get(
    '/get-all-roles',
    response_model=List[_role_schemas.RoleRespDetail],
    status_code=status.HTTP_200_OK
)
async def get_all_roles():
    return role_service.get_all_roles()


@router.put(
    "/update-role",
    status_code=status.HTTP_200_OK,
    response_model=_role_schemas.RoleInUpdate
)
async def update_role(
    role_in: _role_schemas.RoleInUpdate
):
    return role_service.update_role(role_in)


@router.delete(
    "/delete-role/{role_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domain.Message
)
async def delete_role(
    role_id: str
):
    return role_service.delete_role(role_id)
