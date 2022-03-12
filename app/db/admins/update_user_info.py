from app.models.models import UserTable
from app.models.schemas.admins import StaffInUpdate
from app.utils.db_utils import session


def update_user_info(user_id, info_in: StaffInUpdate):
    try:
        _ = session.query(UserTable)\
            .filter(UserTable.user_id == user_id)\
            .update({
                UserTable.first_name: info_in.first_name,
                UserTable.last_name: info_in.last_name,
                UserTable.birthday: info_in.birthday,
            })
        session.commit()
        return info_in
    except Exception:
        session.rollback()
        raise
