from typing import List
from fastapi import (
    UploadFile,
)

from app.db.images.delete_image import delete_image
from app.db.images.get_image_by_id import get_image_by_id
from app.db.products.create_product import create_product
from app.db.products.get_all_products import get_all_products
from app.db.products.get_product_by_id import get_product_by_id
from app.db.products.delete_product_by_id import delete_product_by_id
from app.db.products.get_products_by_category import get_products_by_category
from app.db.products.update_product_by_id import update_product_by_id
from app.models.domains import (
    base as _base_domains,
)
from app.models.schemas import (
    products as _products_schemas,
    images as _images_schemas,
)
from app.utils import (
    file_utils as _file_utils,
    db_utils as _db_utils,
    auth_utils as _auth_utils,
    image_utils as _image_utils
)
from app.utils.product_utils import get_total_stars


class ProductService():

    def create_product(
        self, current_user,
        product_name: str, product_price: float,
        category_id: int, files: list[UploadFile],
        description: str = None,
    ) -> _products_schemas.ProductRespDetail:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        product_in = _products_schemas.ProductInCreate(**{
            'product_name': product_name,
            'product_price': product_price,
            'description': description,
            'category_id': category_id
        })
        response = _db_utils.row_to_dict(create_product(product_in))
        product_id = response.get('product_id')
        image_responses = []
        for index, file in enumerate(files, start=1):
            image_db = _image_utils.create_product_image(
                product_id, file,
                index
            )
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
            product_id = product_response.get('product_id')
            star_number = get_total_stars(product_id)
            product_response.update({'star_number': star_number})
            response.append(product_response)
        return response

    def get_product_by_id(
        self, product_id: int
    ) -> _products_schemas.ProductRespDetail:
        product = get_product_by_id(product_id)
        response = _db_utils.row_to_dict(product)
        star_number = get_total_stars(product_id)
        response.update({
            'images': _file_utils.map_images(product.images),
            'star_number': star_number
        })
        return response

    def update_product_info(
        self, current_user,
        product_in: _products_schemas.ProductInUpdate,
    ) -> _products_schemas.ProductInUpdate:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        response = update_product_by_id(product_in)
        return response

    def delete_product_image(
        self, current_user,
        image_id: int,
    ) -> _base_domains.Message:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        image = get_image_by_id(image_id)
        _file_utils.remove_file(image.image_path)
        _ = delete_image(image_id)
        return {'message': 'Delete successfully'}

    def add_product_image(
        self, current_user,
        product_id: int, image_order: int,
        file: UploadFile
    ) -> _images_schemas.ImageRespDetail:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        image_db = _image_utils.create_product_image(
            product_id, file,
            image_order
        )
        return image_db

    def delete_product_by_id(
        self, product_id: int,
        current_user
    ) -> _base_domains.Message:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        dirname = f'media/products/{product_id}'
        _ = delete_product_by_id(product_id)
        _ = _file_utils.remove_dir(dirname)
        return {'message': 'Delete successfully'}

    def get_products_by_category(
        self, category_id: int
    ) -> List[_products_schemas.ProductRespDetail]:
        response = get_products_by_category(category_id)
        return response
