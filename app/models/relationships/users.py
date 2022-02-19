
from sqlalchemy import String, Integer, Column
from app.db.connection import db_connection


class UserTable(db_connection.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
