from app.db.customers.get_user_by_id import get_user_by_id
from app.db.admins.create_user import create_user
from app.models.schemas import (
    admins as _admin_schemas,
)


class CustomerService():

    def get_user_by_id(self, user_id: str):
        response = get_user_by_id(user_id)
        return response

    def create_customer(
        self, staff_in: _admin_schemas.StaffInCreate
    ) -> _admin_schemas.StaffRespDetail:
        response = create_user(staff_in, role_name='customer')
        return response
