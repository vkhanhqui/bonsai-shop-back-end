from app.db.categories.create_category import create_category
from app.db.categories.delete_category import delete_category
from app.db.categories.get_all_categories import get_all_categories
from app.db.categories.update_category import update_category
from app.models.schemas import categories as _category_schemas


class CategoryService():

    def create_category(self, category_in: _category_schemas.CategoryInCreate):
        response = create_category(category_in)
        return response

    def get_all_categories(self):
        response = get_all_categories()
        return response

    def update_category(self, category_in: _category_schemas.CategoryInUpdate):
        response = update_category(category_in)
        return response

    def delete_category(self, category_id: int):
        _ = delete_category(category_id)
        return {'message': 'Delete successfully'}
