# application/query/handlers/get_session_by_id_handler.py

from application.query.dto.session_dto import SessionDto

class GetSessionByIdHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle(self, query):
        session = self.repository.find_by_id(query.session_id)

        if session is None:
            raise ValueError("Session not found")

        return SessionDto(
            session_id=session.session_id,
            task_id=session.task_id,
            user_id=session.user_id,
            duration_minutes=session.duration.minutes
        )
