from app.models.models import RatingTable
from app.models.schemas.ratings import RatingInCreate
from app.utils.db_utils import session


def create_rating(
    user_id: int, rating_in: RatingInCreate
) -> RatingTable:
    new_rating = RatingTable(user_id=user_id, **rating_in.dict())
    session.add(new_rating)
    try:
        session.flush()
        session.commit()
        return new_rating
    except Exception:
        session.rollback()
