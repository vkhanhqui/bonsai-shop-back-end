from fastapi import (
    APIRouter,
    status,
)
import os

from fastapi.responses import FileResponse


router = APIRouter()


@router.get(
    "/get-image",
    status_code=status.HTTP_200_OK,
)
def get_image(
    image_path: str
):
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/jpeg")
    return {"error": "File not found!"}
