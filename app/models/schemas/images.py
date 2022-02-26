from app.models.domains import (
    images as _images_domain,
    base as _base_domain,
)


class ImageInCreate(
    _images_domain.ImagePath, _base_domain.ProductId
):
    pass


class ImageRespDetail(
    _images_domain.ImagePath, _base_domain.CreateAt,
):

    class Config:
        orm_mode = True
