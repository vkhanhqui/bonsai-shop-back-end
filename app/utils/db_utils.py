from app.db.connection import db_connection


db_connection.Base.metadata.create_all(db_connection.engine)
session = db_connection.Session()
