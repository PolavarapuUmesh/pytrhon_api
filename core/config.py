import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings

# Load environment variables from .env file
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DATABASE_URL: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DATABASE_URL = f'mysql+pymysql://{quote_plus(self.DB_USER)}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

def get_settings() -> Settings:
    return Settings(
        DB_USER=os.getenv('MYSQL_USER'),
        DB_PASSWORD=os.getenv('MYSQL_PASSWORD'),
        DB_NAME=os.getenv('MYSQL_DB'),
        DB_HOST=os.getenv('MYSQL_SERVER'),
        DB_PORT=os.getenv('MYSQL_PORT')
    )

settings = get_settings()
print(settings.DATABASE_URL)
