from app.models.models import ProductTable
from app.models.schemas.products import ProductInUpdate
from app.utils.db_utils import session


def update_product_by_id(product_id: int, product_in: ProductInUpdate):
    _ = session.query(ProductTable).\
        filter(ProductTable.product_id == product_id).\
        update(**product_in.dict())
    session.commit()
    return product_in
