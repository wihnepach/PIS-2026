from datetime import datetime
from enum import Enum


class SessionStatus(Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    DONE = "DONE"
    FAILED = "FAILED"


class Session:
    def __init__(self, session_id: str, task_id: str, user_id: str, duration: int):
        self.session_id = session_id
        self.task_id = task_id
        self.user_id = user_id
        self.duration = duration
        self.status = SessionStatus.ACTIVE
        self.start_time = datetime.now()

    def finish(self):
        if self.status != SessionStatus.ACTIVE:
            raise Exception("Сессию можно завершить только из состояния ACTIVE")
        self.status = SessionStatus.DONE

    def fail(self):
        self.status = SessionStatus.FAILED