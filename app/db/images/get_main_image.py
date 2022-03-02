from app.models.models import ImageTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_main_image(product_id: str):
    images = session.query(ImageTable).\
        filter(text("product_id=:product_id")).\
        params(product_id=product_id).all()
    if images:
        return images[0].image_path
    return None
