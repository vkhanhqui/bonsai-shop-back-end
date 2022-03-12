from app.db.categories.create_category import create_category
from app.db.categories.delete_category import delete_category
from app.db.categories.get_all_categories import get_all_categories
from app.db.categories.update_category import update_category
from app.models.schemas import categories as _category_schemas
from app.utils import (
    auth_utils as _auth_utils
)


class CategoryService():

    def create_category(
        self, current_user,
        category_in: _category_schemas.CategoryInCreate
    ):
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        response = create_category(category_in)
        return response

    def get_all_categories(self):
        response = get_all_categories()
        return response

    def update_category(
        self, current_user,
        category_in: _category_schemas.CategoryInUpdate
    ):
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        response = update_category(category_in)
        return response

    def delete_category(
        self, current_user,
        category_id: int
    ):
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        _ = delete_category(category_id)
        return {'message': 'Delete successfully'}
