from sqlalchemy.orm import Session

from cqrs.read_model.session_view import SessionView


class SessionProjection:
    def __init__(self, db: Session):
        self.db = db

    def handle(self, event):
        event_type, session_id = event

        existing = self.db.query(SessionView).filter_by(session_id=session_id).first()

        if existing:
            if event_type == "SessionStarted":
                existing.status = "ACTIVE"
            elif event_type == "SessionCompleted":
                existing.status = "DONE"
            elif event_type == "SessionFailed":
                existing.status = "FAILED"
        else:
            status = "ACTIVE"
            if event_type == "SessionCompleted":
                status = "DONE"
            elif event_type == "SessionFailed":
                status = "FAILED"

            self.db.add(SessionView(session_id=session_id, status=status))

        self.db.commit()