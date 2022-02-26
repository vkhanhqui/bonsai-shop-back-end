from typing import List
from app.db.admins.create_staff import create_staff
from app.db.admins.delete_staff import delete_staff
from app.db.admins.get_all_staffs import get_all_staffs
from app.models.schemas import admin as _admin_schemas
from app.models.domains import base as _base_domains


class AdminService():

    def create_staff(
        self, staff_in: _admin_schemas.StaffInCreate
    ) -> _admin_schemas.StaffRespDetail:
        response = create_staff(staff_in)
        return response

    def get_all_staffs(
        self
    ) -> List[_admin_schemas.StaffRespDetail]:
        response = get_all_staffs()
        return response

    def delete_staff(self, staff_id: int) -> _base_domains.Message:
        _ = delete_staff(staff_id)
        return {'message': 'Delete successfully'}
