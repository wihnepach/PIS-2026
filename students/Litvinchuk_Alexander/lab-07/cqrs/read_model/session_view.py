from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SessionView(Base):
    __tablename__ = "session_view"

    session_id = Column(String, primary_key=True, index=True)
    status = Column(String, nullable=False)