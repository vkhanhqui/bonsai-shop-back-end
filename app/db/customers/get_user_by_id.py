from app.models.models import UserTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_user_by_id(user_id: str) -> UserTable:
    user = session.query(UserTable).filter(text("user_id=:user_id")).\
        params(user_id=user_id).all()
    if user:
        return user[0]
    return None
