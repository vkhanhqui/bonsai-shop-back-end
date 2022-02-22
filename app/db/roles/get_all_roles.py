from app.models.models import RoleTable
from app.utils.db_utils import session


def get_all_roles():
    roles = session.query(RoleTable).all()
    return roles
