import os
import shutil
from typing import List

from app.core.config import config
from app.models.models import ImageTable
from app.utils import (
    generate_utils as _generate_utils,
)


def write_file(
    destination_dir: str, filename: str,
    data
) -> str:
    is_exist = os.path.exists(destination_dir)
    if not is_exist:
        os.makedirs(destination_dir)
    filename = get_new_filename(filename)
    save_to = f'{destination_dir}/{filename}'
    with open(save_to, "wb+") as f:
        f.write(data)
    return save_to


def get_file_extension(filename: str) -> str:
    """Get extension from filename
    Ex: example.pdf => pdf
    """
    return filename.split(".")[-1]


def get_new_filename(filename: str):
    ksuid = _generate_utils.generate_ksuid()
    file_extension = get_file_extension(filename)
    return f'{ksuid}.{file_extension}'


def remove_dir(dirname: str) -> None:
    shutil.rmtree(dirname)


def map_image(image: ImageTable) -> dict:
    image_path = f"{config.base_url}/bonsai-backend/\
        files/get-image?image_path={image.image_path}"
    return {'image_path': image_path.replace(' ', '')}


def map_images(images: List[ImageTable]) -> List[dict]:
    return list(
        map(map_image, images)
    )
