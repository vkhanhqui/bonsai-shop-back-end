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
    stt: int = 0

    class Config:
        orm_mode = True


class CategoryInUpdate(
    _categories_domain.CategoryName, _base.CategoryId,
):
    pass
