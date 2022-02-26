from typing import List
from fastapi import (
    APIRouter,
    status,
)

from app.services.products import ProductService
from app.models.schemas import (
    products as _product_schemas,
)

from app.models.domains import (
    base as _base_domain
)

router = APIRouter()
product_service = ProductService()


@router.post(
    "/create_product",
    status_code=status.HTTP_201_CREATED,
    response_model=_product_schemas.ProductResDetail
)
async def create_product(product_in: _product_schemas.ProductInCreate):
       return product_service.create_product(product_in)

@router.get(
   "/get-all-products",
    status_code=status.HTTP_200_OK,
    response_model=List[_product_schemas.ProductResDetail],
)
async def get_all_products():
        return product_service.get_all_products()

@router.get(
    "/{product_id}",
     status_code=status.HTTP_200_OK,
     response_model=_product_schemas.ProductResDetail
)
async def get_product_by_id(product_id: int):
        return product_service.get_product_by_id(product_id)

@router.put(
    "/update_product/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=_product_schemas.ProductResDetail
)
async def update_product(product_id: int,product_in: _product_schemas.ProductInUpdate):
        return product_service.update_product(product_id,product_in)

@router.delete(
    "/remove_product/{product_id}",
     status_code=status.HTTP_200_OK,
     response_model=_base_domain.Message
)
async def remove_product(product_id: int):
        return product_service.remove_product(product_id)