from app.models.models import ImageTable
from app.utils.db_utils import session


def delete_image(image_id: int) -> None:
    _ = session.query(ImageTable)\
         .filter(ImageTable.image_id == image_id)\
         .delete()
    _ = session.commit()
