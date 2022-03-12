from app.models.models import ImageTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_image_by_id(image_id: str) -> ImageTable:
    images = session.query(ImageTable).\
        filter(text("image_id=:image_id")).\
        params(image_id=image_id).all()
    if images:
        return images[0]
    return None
