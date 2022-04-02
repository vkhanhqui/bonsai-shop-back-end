from app.models.models import ProductTable
from app.models.schemas.products import ProductFilterResp
from app.utils.db_utils import session


def get_all_products(product_in: ProductFilterResp):
    limit = 90
    page = product_in.page
    offset = (page-1) * limit
    order_by = None
    sort_name = product_in.sort_name
    sort_price = product_in.sort_price
    category_id = product_in.category_id
    search_text = "%{}%".format(product_in.search_text)
    # Handle sort
    if sort_name:
        if sort_name == 'asc':
            order_by = ProductTable.product_name.asc()
        else:
            order_by = ProductTable.product_name.desc()
    elif sort_price:
        if sort_price == 'asc':
            order_by = ProductTable.product_price.asc()
        else:
            order_by = ProductTable.product_price.desc()
    # Main query
    products = session.query(ProductTable)
    # Filter by category
    if category_id > 0:
        products = products.\
            filter(
                ProductTable.category_id == category_id
            )
    if search_text:
        products = products.\
            filter(
                ProductTable.product_name.like(search_text)
            )
    # Apply sort
    if sort_name or sort_price:
        products = products.order_by(order_by)
    # Apply pagination
    products = products.offset(offset).limit(limit).all()
    return products
