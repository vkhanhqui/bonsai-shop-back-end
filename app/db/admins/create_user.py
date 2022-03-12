from fastapi import HTTPException
from app.models.models import UserTable
from app.models.schemas.admins import StaffInCreate
from app.utils.db_utils import session
from app.utils.auth_utils import get_password_hash


def create_user(
    staff_in: StaffInCreate, role_name: str
) -> UserTable:
    staff_data = staff_in.dict()
    roles = {
        'admin': 1,
        'staff': 2,
        'customer': 3,
    }
    staff_data.update({
        'role_id': roles.get(role_name),
        'hashed_password': get_password_hash(staff_data.pop('password'))
    })
    new_staff = UserTable(**staff_data)
    session.add(new_staff)
    try:
        session.flush()
        session.commit()
        return new_staff
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail='User already existed')
