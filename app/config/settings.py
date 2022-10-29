from pydantic import BaseSettings, Field


class DBSettings(BaseSettings):
    DB_NAME: str = Field('db', env='POSTGRES_DB')
    DB_USER: str = Field('user', env='POSTGRES_USER')
    DB_PASSWORD: str = Field('secret', env='POSTGRES_PASSWORD')
    DB_HOST: str = Field('localhost', env='POSTGRES_HOST')
    DB_PORT: int = Field(5432, env='POSTGRES_PORT')


class Settings(DBSettings):
    """
    https://pydantic-docs.helpmanual.io/usage/settings/
    """
