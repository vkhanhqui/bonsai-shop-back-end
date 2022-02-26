from app.models.models import ProductTable
from app.utils.db_utils import session


def remove_product(product_id: int):
    session.query(ProductTable).filter_by(product_id = product_id).delete()
    session.commit()