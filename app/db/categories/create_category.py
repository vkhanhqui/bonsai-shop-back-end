from app.models.models import CategoryTable
from app.models.schemas.categories import CategoryInCreate
from app.utils.db_utils import session


def create_category(category_in: CategoryInCreate) -> CategoryTable:
    new_category = CategoryTable(**category_in.dict())
    session.add(new_category)
    try:
        session.flush()
        session.commit()
        return new_category
    except Exception:
        session.rollback()
        raise
