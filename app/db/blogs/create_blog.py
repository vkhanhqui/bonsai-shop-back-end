from fastapi import HTTPException
from app.models.models import BlogTable
from app.utils.db_utils import session


def create_blog(blog_in: dict) -> BlogTable:
    new_blog = BlogTable(**blog_in)
    session.add(new_blog)
    try:
        session.flush()
        session.commit()
        return new_blog
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail='Blog already existed')
