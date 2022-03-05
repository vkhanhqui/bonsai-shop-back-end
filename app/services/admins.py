from typing import List
from app.db.admins.create_user import create_user
from app.db.admins.delete_staff import delete_staff
from app.db.admins.get_all_staffs import get_all_staffs
from app.db.bills.admin_get_all_bills import get_all_bills
from app.db.bills.update_bill_by_id import update_bill_by_id
from app.models.domains import base as _base_domains
from app.models.schemas import (
    admins as _admin_schemas,
    bills as _bills_schemas,
)
from app.utils import bill_utils as _bill_utils
from app.core.config import config


class AdminService():

    def create_staff(
        self, staff_in: _admin_schemas.StaffInCreate
    ) -> _admin_schemas.StaffRespDetail:
        response = create_user(staff_in, role_name='staff')
        return response

    def get_all_staffs(
        self
    ) -> List[_admin_schemas.StaffRespDetail]:
        response = get_all_staffs()
        return response

    def delete_staff(self, staff_id: int) -> _base_domains.Message:
        _ = delete_staff(staff_id)
        return {'message': 'Delete successfully'}

    def get_all_bills(
        self
    ) -> List[_bills_schemas.AdminBillRespDetail]:
        bills = get_all_bills()
        return _bill_utils.get_bills_in_detail(bills, is_admin=True)

    def confirm_bill(
        self, bill_id: int
    ) -> _base_domains.Message:
        bill_status = config.bill_status.get('admin_confirmed')
        _ = update_bill_by_id(bill_id, bill_status)
        return {'message': bill_status}
