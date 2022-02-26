from app.models.models import RoleTable
from app.utils.db_utils import session


def delete_role(role_id: int) -> None:
    _ = session.query(RoleTable)\
       .filter(RoleTable.role_id == role_id)\
       .delete()
    _ = session.commit()
