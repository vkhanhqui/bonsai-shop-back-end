from typing import List
from fastapi import (
    UploadFile,
)
from app.db.images.create_image import create_image

from app.db.products.create_product import create_product
from app.db.products.get_all_products import get_all_products
from app.db.products.get_product_by_id import get_product_by_id
# from app.db.products.update_product_by_id import update_product_by_id
from app.db.products.delete_product_by_id import delete_product_by_id
from app.db.products.get_products_by_category import get_products_by_category
from app.models.domains import (
    base as _base_domainss,
)
from app.models.schemas import (
    products as _products_schemas,
    images as _images_schemas,
)
from app.utils import (
    file_utils as _file_utils,
    db_utils as _db_utils,
)


class ProductService():

    def create_product(
        self,
        product_name: str, product_price: float,
        category_id: int, files: list[UploadFile],
        description: str = None,
    ) -> _products_schemas.ProductRespDetail:
        product_in = _products_schemas.ProductInCreate(**{
            'product_name': product_name,
            'product_price': product_price,
            'description': description,
            'category_id': category_id
        })
        response = _db_utils.row_to_dict(create_product(product_in))
        product_id = response.get('product_id')
        image_responses = []
        for file in files:
            destination_dir = f'media/products/{product_id}/images'
            image_path = _file_utils.write_file(
                destination_dir, file.filename,
                file.file.read()
            )
            image_in = _images_schemas.ImageInCreate(**{
                'product_id': product_id,
                'image_path': image_path,
            })
            image_db = _file_utils.map_image(create_image(image_in))
            image_responses.append(image_db)
        response.update({'images': image_responses})
        return response

    def get_all_products(
        self
    ) -> List[_products_schemas.ProductRespDetail]:
        products = get_all_products()
        response = []
        for product in products:
            product_response = _db_utils.row_to_dict(product)
            product_response.update({
                'images': _file_utils.map_images(product.images)
            })
            response.append(product_response)
        return response

    def get_product_by_id(
        self, product_id: int
    ) -> _products_schemas.ProductRespDetail:
        product = get_product_by_id(product_id)
        response = _db_utils.row_to_dict(product)
        response.update({
            'images': _file_utils.map_images(product.images)
        })
        return response

    # def update_product_by_id(
    #     self, product_id: int,
    #     product_in: _products_schemas.ProductInUpdate
    # ) -> _products_schemas.ProductRespDetail:
    #     response = update_product_by_id(product_id, product_in)
    #     return response

    def delete_product_by_id(
        self, product_id: int
    ) -> _base_domainss.Message:
        dirname = f'media/products/{product_id}'
        _ = delete_product_by_id(product_id)
        _ = _file_utils.remove_dir(dirname)
        return {'message': 'Delete successfully'}

    def get_products_by_category(
        self, category_id: int
    ) -> List[_products_schemas.ProductRespDetail]:
        response = get_products_by_category(category_id)
        return response
