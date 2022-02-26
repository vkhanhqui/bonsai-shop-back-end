from app.models.models import UserTable
from app.utils.db_utils import session


def delete_staff(staff_id: int) -> None:
    _ = session.query(UserTable)\
         .filter(UserTable.user_id == staff_id)\
         .delete()
    _ = session.commit()
