from app.db.products.create_product import create_product
from app.db.products.get_all_products import get_all_products
from app.db.products.get_product_by_id import get_product_by_id
from app.db.products.update_product_by_id import update_product_by_id
from app.db.products.delete_product_by_id import delete_product_by_id
from app.models.schemas import products as _product_schemas


class ProductService():

    def create_product(
        self, product_in: _product_schemas.ProductInCreate
    ):
        response = create_product(product_in)
        return response

    def get_all_products(self):
        response = get_all_products()
        return response

    def get_product_by_id(self, product_id: int):
        response = get_product_by_id(product_id)
        return response

    def update_product_by_id(
        self, product_id: int,
        product_in: _product_schemas.ProductInUpdate
    ):
        response = update_product_by_id(product_id, product_in)
        return response

    def delete_product_by_id(self, product_id: int):
        response = delete_product_by_id(product_id)
        return response
