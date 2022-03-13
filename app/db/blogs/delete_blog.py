from app.models.models import BlogTable
from app.utils.db_utils import session


def delete_blog(blog_id: int) -> None:
    try:
        _ = session.query(BlogTable)\
         .filter(BlogTable.blog_id == blog_id)\
         .delete()
        _ = session.commit()
    except Exception:
        session.rollback()
        raise
