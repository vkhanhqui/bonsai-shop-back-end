from app.models.models import RoleTable
from app.models.schemas.roles import RoleInCreate
from app.utils.db_utils import session


def create_role(role_in: RoleInCreate) -> RoleTable:
    new_role = RoleTable(**role_in.dict())
    session.add(new_role)
    try:
        session.flush()
        session.commit()
        return new_role
    except:
        session.rollback()
        raise
