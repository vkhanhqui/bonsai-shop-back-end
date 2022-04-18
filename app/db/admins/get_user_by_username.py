from app.models.models import UserTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_user_by_username(username: str) -> UserTable:
    user = session.query(UserTable).filter(text("username=:username")).\
        params(username=username).all()
    if user:
        return user[0]
    return None
