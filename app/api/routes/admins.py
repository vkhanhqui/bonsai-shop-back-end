from typing import List
from fastapi import (
    APIRouter,
    status,
)

from app.services.admins import AdminService
from app.models.domains import base as _base_domain
from app.models.schemas import (
    admin as _admin_schemas,
)


router = APIRouter()
admin_service = AdminService()


@router.post(
    "/create-staff",
    status_code=status.HTTP_201_CREATED,
    response_model=_admin_schemas.StaffRespDetail
)
async def create_staff(
    staff_in: _admin_schemas.StaffInCreate
):
    return admin_service.create_staff(staff_in)


@router.get(
    '/get-all-staffs',
    response_model=List[_admin_schemas.StaffRespDetail],
    status_code=status.HTTP_200_OK
)
async def get_all_staffs():
    return admin_service.get_all_staffs()


@router.delete(
    "/delete-staff/{staff_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domain.Message
)
async def delete_staff(
    staff_id: int
):
    return admin_service.delete_staff(staff_id)
