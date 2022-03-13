from fastapi import UploadFile

from app.utils import (
    file_utils as _file_utils,
    auth_utils as _auth_utils,
)
from app.models.schemas import (
    images as _images_schemas,
)


class BlogService():

    def upload_image(
        self, current_user,
        file: UploadFile
    ) -> _images_schemas.BlogImageResp:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        destination_dir = f'media/blogs/{current_user.username}/images'
        image_path = _file_utils.write_file(
            destination_dir, file.filename,
            file.file.read()
        )
        image_db = _file_utils.map_image(image_path)
        return image_db
