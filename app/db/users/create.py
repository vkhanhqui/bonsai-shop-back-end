from app.models.models import UserTable
from app.models.schemas.users import UserInCreate
from app.utils.db_utils import session


def create_user(user_in: UserInCreate) -> UserTable:
    new_user = UserTable(**user_in.dict())
    session.add(new_user)
    try:
        session.flush()
        session.commit()
        return new_user
    except:
        session.rollback()
        raise
