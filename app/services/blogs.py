from typing import List
from fastapi import UploadFile
from app.db.blogs.create_blog import create_blog
from app.db.blogs.delete_blog import delete_blog
from app.db.blogs.get_all_blogs import get_all_blogs
from app.db.blogs.update_blog import update_blog

from app.utils import (
    file_utils as _file_utils,
    auth_utils as _auth_utils,
    db_utils as _db_utils,
    image_utils as _image_utils,
)
from app.models.domains import base as _base_domains
from app.models.schemas import (
    images as _images_schemas,
    blogs as _blogs_schemas,
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

    def create_blog(
        self, current_user,
        blog_in: _blogs_schemas.BlogInCreate,
    ) -> _blogs_schemas.BlogRespDetail:
        user_id = current_user.user_id
        _auth_utils.is_admin_or_staff(
            user_id, is_raise_err=True
        )
        response = blog_in.dict()
        save_blog = response.copy()
        save_blog.update({
            'staff_or_admin_id': user_id,
            'image_path': _image_utils.get_image_path_from_url(
                blog_in.image_path)
        })
        db_blog = create_blog(save_blog)
        response.update({'blog_id': db_blog.blog_id})
        return response

    def update_blog(
        self, current_user,
        blog_in: _blogs_schemas.BlogInUpdate,
    ) -> _blogs_schemas.BlogRespDetail:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        db_blog = update_blog(blog_in)
        return db_blog

    def delete_blog(
        self, current_user,
        blog_id: int,
    ) -> _base_domains.Message:
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        _ = delete_blog(blog_id)
        return {'message': 'Delete successfully'}

    def get_all_blogs(
        self,
    ) -> List[_blogs_schemas.BlogRespDetail]:
        blogs = get_all_blogs()
        response = []
        for blog in blogs:
            blog_response = _db_utils.row_to_dict(blog)
            blog_response.update(
                _file_utils.map_image(blog.image_path)
            )
            response.append(blog_response)
        return response
