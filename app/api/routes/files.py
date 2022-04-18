from fastapi import (
    APIRouter,
    status,
    UploadFile,
)
from fastapi.responses import FileResponse
from app.services.images import ImageService
from app.utils import (
    file_utils as _file_utils,
)

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


@router.post(
    "/upload-image",
    status_code=status.HTTP_200_OK,
)
def upload_image(
    file: UploadFile
):
    destination_dir = 'temp'
    image_path = _file_utils.write_file(
        destination_dir, file.filename,
        file.file.read()
    )
    return FileResponse(image_path, media_type="image/jpeg")
