from app.models.relationships.users import UserTable
from app.models.schemas.users import UserSignUpIn
from app.utils.db_utils import session


def create_user(user_in: UserSignUpIn):
    new_user = UserTable(**user_in.dict())
    session.add(new_user)
    try:
        session.commit()
    except:
        session.rollback()
        raise
