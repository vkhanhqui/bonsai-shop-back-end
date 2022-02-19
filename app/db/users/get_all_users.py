from app.models.relationships.users import UserTable
from app.utils.db_utils import session


def get_all_users():
    users = session.query(UserTable).all()
    return users
