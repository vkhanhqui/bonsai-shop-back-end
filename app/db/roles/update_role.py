from app.models.models import RoleTable
from app.models.schemas.roles import RoleInUpdate
from app.utils.db_utils import session


def update_role(role_in: RoleInUpdate):
    _ = session.query(RoleTable)\
       .filter(RoleTable.role_id == role_in.role_id)\
       .update({RoleTable.role_name: role_in.role_name})
    session.commit()
    return role_in
