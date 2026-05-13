from pydantic_settings import BaseSettings
from sqlalchemy.orm import DeclarativeMeta, declarative_base


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///horizon_db.sqlite3"

    DBBaseModel: DeclarativeMeta = declarative_base()


settings = Settings()
