# application/query/dto/session_dto.py

class SessionDto:
    def __init__(self, session_id: str, task_id: str, user_id: str, duration_minutes: int):
        self.session_id = session_id
        self.task_id = task_id
        self.user_id = user_id
        self.duration_minutes = duration_minutes
