import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Bonsai Backend APIs"
    api_prefix: str = "/bonsai-backend"
    debug: bool = True
    # to get a string like this run:
    # openssl rand -hex 32
    secret = '436d771eed17d16d7ad00d45ce0ca7a6d0dda2fb5901ff2d87375453a713fd0c'
    algorithm = "HS256"
    access_token_expire_minutes = 30


class LocalSetting(Settings):
    database_username = 'root'
    database_pwd = 'root'
    database_name = 'bonsai_db'
    database_host = 'localhost:3306'


class DockerSettings(Settings):
    database_username = 'root'
    database_pwd = 'root'
    database_name = 'bonsai_db'
    database_host = 'db:3306'


def get_settings():
    env = os.getenv("env", None)
    if env == 'docker':
        return DockerSettings()
    else:
        return LocalSetting()


config = get_settings()
