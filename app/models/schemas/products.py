from typing import List
from fastapi import HTTPException

from pydantic import BaseModel, Field, validator

from app.models.domains import (
    products as _products_domains,
    base as _base_domains,
    ratings as _ratings_domains,
)

from app.models.schemas import (
    images as _images_schemas,
)


class ProductInCreate(
    _products_domains.ProductName, _products_domains.ProductPrice,
    _products_domains.Description, _base_domains.CategoryId,
):
    pass


class ProductRespDetail(
    _products_domains.ProductName, _products_domains.ProductPrice,
    _products_domains.Description, _base_domains.ProductId,
    _ratings_domains.StartNumber, _base_domains.CategoryId,
):
    images: List[_images_schemas.ImageRespDetail]
    stt: int = Field(default=1)

    class Config:
        orm_mode = True


class PaginationProducts(_base_domains.Total):
    products: List[ProductRespDetail]


class ProductInUpdate(
    _products_domains.ProductName, _products_domains.ProductPrice,
    _products_domains.Description, _base_domains.ProductId,
):
    pass


class ProductFilterResp(BaseModel):
    category_id: int = 0
    sort_price: str = ''
    sort_name: str = ''
    range_price_from: str = ''
    range_price_to: str = ''
    search_text: str = ''
    page: int = 1

    @validator("page", pre=True)
    def check_str(cls, x):
        int_x = int(x)
        if (int_x < 1):
            raise HTTPException(
                status_code=400,
                detail='Page must be greater than 0'
            )
        return x
