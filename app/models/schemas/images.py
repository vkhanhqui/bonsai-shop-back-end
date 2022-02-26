from app.models.domains import (
    images as _images_domain,
    base as _base_domains,
)


class ImageInCreate(
    _images_domain.ImagePath, _base_domains.ProductId
):
    pass


class ImageRespDetail(
    _images_domain.ImagePath, _base_domains.CreateAt,
):

    class Config:
        orm_mode = True
