from app.models.models import CategoryTable
from app.utils.db_utils import session


def delete_category(category_id: int) -> None:
    _ = session.query(CategoryTable)\
       .filter(CategoryTable.category_id == category_id)\
       .delete()
    _ = session.commit()
