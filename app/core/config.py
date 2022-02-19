from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Bonsai Backend APIs"
    api_prefix: str = "/bonsai-backend"
    debug: bool = True
    database_username = 'root'
    database_pwd = 'root'
    database_name = 'bonsai_db'


config = Settings()
