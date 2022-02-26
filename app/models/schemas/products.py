from typing import List

from app.models.domains import (
    products as _products_domains,
    base as _base_domainss,
)

from app.models.schemas import (
    images as _images_schemas,
)


class ProductInCreate(
    _products_domains.ProductName, _products_domains.ProductPrice,
    _products_domains.Description, _base_domainss.CategoryId,
):
    pass


class ProductRespDetail(
    _products_domains.ProductName, _products_domains.ProductPrice,
    _products_domains.Description, _base_domainss.ProductId,
):
    images: List[_images_schemas.ImageRespDetail]

    class Config:
        orm_mode = True


class ProductInUpdate(
    _products_domains.ProductName, _products_domains.ProductPrice,
    _products_domains.Description,
):
    pass
