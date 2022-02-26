from app.db.users.get_user_by_id import get_user_by_id


class CustomerService():

    def get_user_by_id(self, user_id: str):
        response = get_user_by_id(user_id)
        return response
