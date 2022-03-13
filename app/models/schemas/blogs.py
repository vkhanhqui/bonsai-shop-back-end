from app.models.domains import (
    blogs as _blogs_domain,
    base as _base,
    images as _images_domain,
)


class BlogInCreate(
    _blogs_domain.BlogTitle, _blogs_domain.BlogContent,
    _blogs_domain.BlogDescription, _images_domain.ImagePath
):
    pass


class BlogRespDetail(
    BlogInCreate, _base.BlogId,
    # _base.CreateAt,
):

    class Config:
        orm_mode = True


class BlogInUpdate(
    _base.BlogId, _blogs_domain.BlogTitle,
    _blogs_domain.BlogContent, _blogs_domain.BlogDescription,
    _images_domain.ImagePath
):
    pass
