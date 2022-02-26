from app.models.models import ProductTable
from app.utils.db_utils import session


def get_by_id(product_id: int):
    product = session.query(ProductTable).get(product_id)
    return product
