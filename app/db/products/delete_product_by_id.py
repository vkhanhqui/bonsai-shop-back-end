from app.models.models import ProductTable, ImageTable
from app.utils.db_utils import session


def delete_product_by_id(product_id: int):
    session.query(ImageTable).filter_by(product_id=product_id).delete()
    session.commit()
    session.query(ProductTable).filter_by(product_id=product_id).delete()
    session.commit()
