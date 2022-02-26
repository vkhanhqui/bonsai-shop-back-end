from app.db.users.create import create_user
from app.db.users.get_all import get_all_users
from app.db.users.get_by_id import get_by_id
from app.models.schemas import users as _user_schemas

class UserService():

    def create_user(self, user_in: _user_schemas.UserInCreate):
        response = create_user(user_in)
        return response

    def get_all_users(self):
        response = get_all_users()
        return response
    def get_user_by_id(self, user_id: int):
        response = get_by_id(user_id)
        return response
