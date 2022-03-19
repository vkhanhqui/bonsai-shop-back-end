from app.models.models import RatingTable
from app.models.schemas.ratings import (
    RatingCustomerInUpdate,
    RatingStaffInUpdate
)
from app.utils.db_utils import session


def update_rating_as_customer(user_id: int, rating_in: RatingCustomerInUpdate):
    try:
        _ = session.query(RatingTable)\
            .filter(
                RatingTable.product_id == rating_in.product_id and
                RatingTable.user_id == user_id)\
            .update({
                RatingTable.message: rating_in.message,
                RatingTable.star_number: rating_in.star_number
            })
        session.commit()
        return rating_in
    except Exception:
        session.rollback()


def update_rating_as_staff(rating_in: RatingStaffInUpdate):
    try:
        _ = session.query(RatingTable)\
            .filter(RatingTable.rating_id == rating_in.rating_id)\
            .update({
                RatingTable.message: rating_in.message,
                RatingTable.star_number: rating_in.star_number
            })
        session.commit()
        return rating_in
    except Exception:
        session.rollback()
