from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    app_name: str = "Bonsai Backend APIs"
    api_prefix: str = "/bonsai-backend"
    debug: bool = True


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
