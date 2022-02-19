from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import config


class DBConnection():
    engine = create_engine(
        f"mysql+pymysql://{config.database_username}"
        f":{config.database_pwd}@{config.database_host}"
        f"/{config.database_name}",
        echo=True
    )

    Base = declarative_base()
    Session = sessionmaker(bind=engine)


db_connection = DBConnection()
