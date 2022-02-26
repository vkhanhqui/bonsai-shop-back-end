from app.models.models import UserTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_all_staffs():
    session.query(UserTable).filter(text("role_id=:role_id")).\
        params(role_id=2).all()
    roles = session.query(UserTable).all()
    return roles
