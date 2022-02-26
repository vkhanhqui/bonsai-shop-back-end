from app.db.products.create import create_product
from app.db.products.get_all import get_all_products
from app.db.products.get_by_id import get_by_id
from app.db.products.update import update_product
from app.db.products.remove import remove_product
from app.models.schemas import products as _product_schemas

class ProductService():

    def create_product(self, product_in: _product_schemas.ProductInCreate):
        response = create_product(product_in)
        return response

    def get_all_products(self):
        response = get_all_products()
        return response
    def get_product_by_id(self, product_id: int):
        response = get_by_id(product_id)
        return response

    def update_product(self, product_id: int, product_in: _product_schemas.ProductInUpdate):
        response = update_product(product_id,product_in)
        return response

    def remove_product(self, product_id: int):
            response = remove_product(product_id)
            return response