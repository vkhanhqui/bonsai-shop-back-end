from fastapi import HTTPException
from app.models.models import BlogTable
from app.models.schemas.blogs import BlogInUpdate
from app.utils.db_utils import session
from app.utils.image_utils import get_image_path_from_url


def update_blog(blog_in: BlogInUpdate):
    try:
        blog_in = session.query(BlogTable)\
            .filter(BlogTable.blog_id == blog_in.blog_id)\
            .update({
                BlogTable.title: blog_in.title,
                BlogTable.content: blog_in.content,
                BlogTable.description: blog_in.description,
                BlogTable.image_path: get_image_path_from_url(
                    blog_in.image_path),
            })
        session.commit()
        return blog_in
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail='Blog already existed')
