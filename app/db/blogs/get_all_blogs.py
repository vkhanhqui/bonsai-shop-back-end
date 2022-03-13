from app.models.models import BlogTable
from app.utils.db_utils import session


def get_all_blogs():
    blogs = session.query(BlogTable).all()
    return blogs
