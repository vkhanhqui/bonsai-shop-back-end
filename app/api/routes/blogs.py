from typing import List
from fastapi import (
    APIRouter,
    status,
    UploadFile,
    Depends,
)

from app.models.schemas import (
    auth as _auth_schemas,
    images as _images_schemas,
    blogs as _blogs_schemas,
)
from app.services.blogs import BlogService
from app.models.domains import base as _base_domains
from app.utils import auth_utils as _auth_utils


router = APIRouter()
blog_service = BlogService()


@router.post(
    "/upload-image",
    status_code=status.HTTP_201_CREATED,
    response_model=_images_schemas.BlogImageResp
)
async def upload_image(
    file: UploadFile,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return blog_service.upload_image(
        current_user, file
    )


@router.post(
    "/create-blog",
    status_code=status.HTTP_201_CREATED,
    response_model=_blogs_schemas.BlogRespDetail
)
async def create_blog(
    blog_in: _blogs_schemas.BlogInCreate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return blog_service.create_blog(
        current_user, blog_in
    )


@router.put(
    "/update-blog",
    status_code=status.HTTP_200_OK,
    response_model=_blogs_schemas.BlogRespDetail
)
async def update_blog(
    blog_in: _blogs_schemas.BlogInUpdate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return blog_service.update_blog(
        current_user, blog_in
    )


@router.delete(
    "/delete-blog/{blog_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domains.Message
)
async def delete_blog(
    blog_id: int,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return blog_service.delete_blog(
        current_user, blog_id
    )


@router.get(
    "/get-all-blogs",
    status_code=status.HTTP_200_OK,
    response_model=List[_blogs_schemas.BlogRespDetail]
)
async def get_all_blogs():
    return blog_service.get_all_blogs()
