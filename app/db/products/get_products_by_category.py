from app.models.models import ProductTable
from app.utils.db_utils import session


def get_products_by_category(category_id: int):
    products = session.query(ProductTable).\
        filter(ProductTable.category_id == category_id).\
        all()
    return products
