from pydantic import BaseSettings


class Settings(BaseSettings):

    some_settings_field: str = ''

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
