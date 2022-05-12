from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Image


session: SessionLocal = SessionLocal()


def get_all_images():
    respon: list[Image] = session.query(Image).all()
    return respon, session
