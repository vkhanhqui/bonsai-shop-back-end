from app.db.connection import db_connection


db_connection.Base.metadata.create_all(db_connection.engine)
session = db_connection.Session()


def row_to_dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d
