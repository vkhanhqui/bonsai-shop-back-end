from app.models.models import ProductTable
from app.utils.db_utils import session


def get_all_products():
    products = session.query(ProductTable).all()
    return products
