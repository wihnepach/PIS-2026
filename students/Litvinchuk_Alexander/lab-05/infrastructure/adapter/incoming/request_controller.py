from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from infrastructure.config.database import SessionLocal
from infrastructure.adapter.outgoing.request_repository import SessionRepository, SessionOrm


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CreateSessionRequest(BaseModel):
    session_id: str
    task_id: str
    user_id: str
    duration_minutes: int
    status: str = "ACTIVE"


@router.post("/api/requests")
def create_request(request: CreateSessionRequest, db: Session = Depends(get_db)):
    repository = SessionRepository(db)

    session = SessionOrm(
        session_id=request.session_id,
        task_id=request.task_id,
        user_id=request.user_id,
        duration_minutes=request.duration_minutes,
        status=request.status,
    )

    repository.save(session)
    return {"request_id": request.session_id}


@router.get("/api/requests/{request_id}")
def get_request_by_id(request_id: str, db: Session = Depends(get_db)):
    repository = SessionRepository(db)
    session = repository.find_by_id(request_id)

    if not session:
        raise HTTPException(status_code=404, detail="Request not found")

    return {
        "session_id": session.session_id,
        "task_id": session.task_id,
        "user_id": session.user_id,
        "duration_minutes": session.duration_minutes,
        "status": session.status,
    }


@router.get("/api/requests")
def get_requests(db: Session = Depends(get_db)):
    repository = SessionRepository(db)
    sessions = repository.find_all()

    return [
        {
            "session_id": session.session_id,
            "task_id": session.task_id,
            "user_id": session.user_id,
            "duration_minutes": session.duration_minutes,
            "status": session.status,
        }
        for session in sessions
    ]