from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from infrastructure.config.database import Base


class SessionOrm(Base):
    __tablename__ = "sessions"

    session_id = Column(String, primary_key=True, index=True)
    task_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    status = Column(String, nullable=False)


class SessionRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, session):
        existing = self.db.query(SessionOrm).filter_by(session_id=session.session_id).first()

        if existing:
            existing.task_id = session.task_id
            existing.user_id = session.user_id
            existing.duration_minutes = session.duration_minutes
            existing.status = session.status
        else:
            self.db.add(session)

        self.db.commit()

    def find_by_id(self, request_id: str):
        return self.db.query(SessionOrm).filter_by(session_id=request_id).first()

    def find_active_requests(self):
        return self.db.query(SessionOrm).filter_by(status="ACTIVE").all()

    def find_all(self):
        return self.db.query(SessionOrm).all()

    def delete(self, request_id: str):
        session = self.db.query(SessionOrm).filter_by(session_id=request_id).first()
        if session:
            self.db.delete(session)
            self.db.commit()