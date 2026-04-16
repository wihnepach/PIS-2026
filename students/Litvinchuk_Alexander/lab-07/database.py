from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cqrs.read_model.session_view import Base

DATABASE_URL = "sqlite:///session_view.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)