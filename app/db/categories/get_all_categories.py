from app.models.models import CategoryTable
from app.utils.db_utils import session


def get_all_categories():
    categories = session.query(CategoryTable).all()
    return categories
