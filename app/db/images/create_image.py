from app.models.models import ImageTable
from app.models.schemas.images import ImageInCreate
from app.utils.db_utils import session


def create_image(image_in: ImageInCreate) -> ImageTable:
    new_image = ImageTable(**image_in.dict())
    session.add(new_image)
    try:
        session.flush()
        session.commit()
        return new_image
    except Exception:
        session.rollback()
        raise
