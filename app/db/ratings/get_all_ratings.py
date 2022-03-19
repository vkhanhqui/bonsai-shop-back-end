from app.models.models import RatingTable
from app.utils.db_utils import session


def get_all_ratings(product_id: int):
    ratings = session.query(RatingTable).\
        filter(RatingTable.product_id == product_id).\
        all()
    return ratings
