from app.models.models import ProductTable
from app.models.schemas.products import ProductInCreate
from app.utils.db_utils import session


def create_product(product_in: ProductInCreate) -> ProductTable:
    new_product = ProductTable(**product_in.dict())
    session.add(new_product)
    try:
        session.flush()
        session.commit()
        return new_product
    except:
        session.rollback()
        raise
