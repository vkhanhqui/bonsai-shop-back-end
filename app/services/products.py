from app.db.products.create import create_product
from app.db.products.get_all import get_all_products
from app.models.schemas import products as _product_schemas

class ProductService():

    def create_product(self, product_in: _product_schemas.ProductInCreate):
        response = create_product(product_in)
        return response

    def get_all_products(self):
        response = get_all_products()
        return response