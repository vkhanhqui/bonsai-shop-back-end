from app.models.models import RatingTable
from app.utils.db_utils import session


def delete_rating(rating_id: int) -> None:
    try:
        _ = session.query(RatingTable)\
            .filter(RatingTable.rating_id == rating_id)\
            .delete()
        _ = session.commit()
    except Exception:
        session.rollback()
        raise
