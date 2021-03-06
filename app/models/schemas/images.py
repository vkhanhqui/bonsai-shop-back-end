from app.models.domains import (
    images as _images_domain,
    base as _base_domains,
)


class ImageInCreate(
    _images_domain.ImagePath, _base_domains.ProductId,
    _images_domain.ImageOrder
):
    pass


class ImageRespDetail(
    _images_domain.ImagePath,
    _images_domain.ImageOrder
):

    class Config:
        orm_mode = True


class BlogImageResp(
    _images_domain.ImagePath,
):
    pass
