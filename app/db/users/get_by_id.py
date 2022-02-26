from app.models.models import UserTable
from app.utils.db_utils import session


def get_by_id(user_id: int):
    user = session.query(UserTable).get(user_id)
    return user
