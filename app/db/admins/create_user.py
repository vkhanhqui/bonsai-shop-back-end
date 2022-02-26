from app.models.models import UserTable
from app.models.schemas.admin import StaffInCreate
from app.utils.db_utils import session


def create_user(staff_in: StaffInCreate, role_name: str) -> UserTable:
    staff_data = staff_in.dict()
    roles = {
        'admin': 1,
        'staff': 2,
        'customer': 3,
    }
    staff_data.update({'role_id': roles.get(role_name)})
    new_staff = UserTable(**staff_data)
    session.add(new_staff)
    try:
        session.flush()
        session.commit()
        return new_staff
    except:
        session.rollback()
        raise
