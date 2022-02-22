from typing import List
from fastapi import (
    APIRouter,
    status,
)

from app.services.products import ProductService
from app.models.schemas import (
    products as _product_schemas,
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