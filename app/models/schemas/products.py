from app.models.domains import (
    products as _products_domains,
)


class ProductInCreate(
    _products_domains.ProductName,
    _products_domains.ProductPrice,
    _products_domains.Description,
):
    pass


class ProductResDetail(
    _products_domains.ProductName,
    _products_domains.ProductPrice,
    _products_domains.Description,
):

    class Config:
        orm_mode = True


class ProductInUpdate(
    _products_domains.ProductName,
    _products_domains.ProductPrice,
    _products_domains.Description,
):
    pass
