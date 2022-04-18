from fastapi import UploadFile
from app.db.images.create_image import create_image

from app.utils import (
    file_utils as _file_utils,
)
from app.models.schemas import (
    images as _images_schemas,
)
from app.core.config import config


def create_product_image(
    product_id: int, file: UploadFile,
    image_order: int
) -> dict:
    destination_dir = f'media/products/{product_id}/images'
    image_path = _file_utils.write_file(
        destination_dir, file.filename,
        file.file.read()
    )
    image_in = _images_schemas.ImageInCreate(**{
        'product_id': product_id,
        'image_path': image_path,
        'image_order': image_order,
    })
    image_db = _file_utils.map_image(create_image(image_in))
    return image_db


def get_image_path_from_url(image_path: str):
    path = f"{config.base_url}/bonsai-backend/\
        files/get-image?image_path=".replace(' ', '')
    return image_path.replace(path, '')
