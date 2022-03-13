from fastapi import (
    APIRouter,
    status,
    UploadFile,
    Depends,
)

from app.models.schemas import (
    auth as _auth_schemas,
    images as _images_schemas,
)
from app.services.blogs import BlogService
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
