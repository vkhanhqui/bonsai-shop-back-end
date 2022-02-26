from app.models.domains import (
    categories as _categories_domain,
    base as _base,
)


class CategoryInCreate(
    _categories_domain.CategoryName,
):
    pass


class CategoryRespDetail(
    _categories_domain.CategoryName, _base.CategoryId,
    _base.CreateAt,
):

    class Config:
        orm_mode = True


class CategoryInUpdate(
    _categories_domain.CategoryName, _base.CategoryId,
):
    pass
