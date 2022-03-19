from app.models.models import RatingTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_rating_by_prod_and_user(product_id: int, user_id: int):
    query_text = 'product_id=:product_id and user_id=:user_id'
    ratings = session.query(RatingTable).\
        filter(text(query_text)).\
        params(product_id=product_id, user_id=user_id).\
        all()
    if ratings:
        return ratings[0]
    return None
