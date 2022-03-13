from fastapi import (
    APIRouter,
    status,
)
from app.services.images import ImageService


router = APIRouter()
image_service = ImageService()


@router.get(
    "/get-image",
    status_code=status.HTTP_200_OK,
)
def get_image(
    image_path: str
):
    return image_service.get_image(image_path)
