from fastapi import (
    APIRouter,
)
import os

from fastapi.responses import FileResponse


router = APIRouter()


@router.get(
    "/get-image"
)
def get_image(
    image_path: str
):
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/jpeg")
    return {"error": "File not found!"}
