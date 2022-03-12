from app.models.models import ProductTable
from app.models.schemas.products import ProductInUpdate
from app.utils.db_utils import session


def update_product_by_id(product_in: ProductInUpdate):
    _ = session.query(ProductTable).\
        filter(ProductTable.product_id == product_in.product_id).\
        update({
            ProductTable.description: product_in.description,
            ProductTable.product_name: product_in.product_name,
            ProductTable.product_price: product_in.product_price,
        })
    session.commit()
    return product_in
