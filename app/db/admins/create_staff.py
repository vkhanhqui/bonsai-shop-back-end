from app.models.models import UserTable
from app.models.schemas.admin import StaffInCreate
from app.utils.db_utils import session


def create_staff(staff_in: StaffInCreate) -> UserTable:
    staff_data = staff_in.dict()
    staff_data.update({'role_id': 2})
    new_staff = UserTable(**staff_data)
    session.add(new_staff)
    try:
        session.flush()
        session.commit()
        return new_staff
    except:
        session.rollback()
        raise
