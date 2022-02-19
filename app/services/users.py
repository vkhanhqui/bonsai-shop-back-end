from app.db.users.create_user import create_user
from app.db.users.get_all_users import get_all_users
from app.models.schemas import users as _uschemas


class UserService():

    def sign_up(self, user_in: _uschemas.UserSignUpIn):
        _ = create_user(user_in)
        return user_in

    def get_all_users(self):
        response = get_all_users()
        return response
