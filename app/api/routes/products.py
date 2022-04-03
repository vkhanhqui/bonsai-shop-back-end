from typing import List
from fastapi import (
    APIRouter,
    status,
    UploadFile,
    Depends,
)

from app.services.products import ProductService
from app.models.schemas import (
    products as _product_schemas,
    auth as _auth_schemas,
    images as _images_schemas,
)

from app.models.domains import (
    base as _base_domains
)
from app.utils import auth_utils as _auth_utils


router = APIRouter()
product_service = ProductService()


@router.post(
    "/create-product",
    status_code=status.HTTP_201_CREATED,
    response_model=_product_schemas.ProductRespDetail
)
async def create_product(
    product_name: str, product_price: float,
    category_id: int, files: list[UploadFile],
    description: str = None,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return product_service.create_product(
        current_user, product_name,
        product_price, category_id,
        files, description
    )


@router.post(
    "/get-all-products",
    status_code=status.HTTP_200_OK,
    response_model=_product_schemas.PaginationProducts,
)
async def get_all_products(
    product_in: _product_schemas.ProductFilterResp
):
    return product_service.get_all_products(product_in)


@router.get(
    "/get-product-by-id/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=_product_schemas.ProductRespDetail
)
async def get_product_by_id(product_id: int):
    return product_service.get_product_by_id(product_id)


@router.put(
    "/update-product-info",
    status_code=status.HTTP_200_OK,
    response_model=_product_schemas.ProductInUpdate
)
async def update_product_info(
    product_in: _product_schemas.ProductInUpdate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return product_service.update_product_info(
        current_user, product_in
    )


@router.delete(
    "/delete-product-image/{image_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domains.Message
)
async def delete_product_image(
    image_id: int,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return product_service.delete_product_image(
        current_user, image_id
    )


@router.post(
    "/add-product-image",
    status_code=status.HTTP_200_OK,
    response_model=_images_schemas.ImageRespDetail
)
async def add_product_image(
    product_id: int, image_order: int,
    file: UploadFile,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return product_service.add_product_image(
        current_user, product_id,
        image_order, file
    )


@router.delete(
    "/delete-product-by-id/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domains.Message
)
async def delete_product_by_id(
    product_id: int,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return product_service.delete_product_by_id(product_id, current_user)


@router.get(
    "/get-products-by-category/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=List[_product_schemas.ProductRespDetail],
)
async def get_products_by_category(category_id: int):
    return product_service.get_products_by_category(category_id)
