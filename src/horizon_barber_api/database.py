from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .settings import settings

engine = create_engine(settings.DATABASE_URL)


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
