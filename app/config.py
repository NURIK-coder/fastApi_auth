from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    SECRET_KEY:str

    class Config:
        env_file = '.env'


settings = Settings()
