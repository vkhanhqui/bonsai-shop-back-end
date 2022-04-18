from fastapi import HTTPException
from app.models.models import CategoryTable
from app.models.schemas.categories import CategoryInUpdate
from app.utils.db_utils import session


def update_category(category_in: CategoryInUpdate):
    try:
        _ = session.query(CategoryTable)\
            .filter(CategoryTable.category_id == category_in.category_id)\
            .update({CategoryTable.category_name: category_in.category_name})
        session.commit()
        return category_in
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail='Category already existed')
