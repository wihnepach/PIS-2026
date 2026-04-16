from datetime import datetime
from domain.models.session_status import SessionStatus
from domain.events.session_events import SessionStarted, SessionCompleted, SessionFailed
from domain.exceptions.domain_exceptions import InvalidSessionStateException


class Session:
    def __init__(self, session_id: str, task_id: str, user_id: str, duration):
        self.session_id = session_id
        self.task_id = task_id
        self.user_id = user_id
        self.duration = duration  # Ожидается объект Duration
        self._status = SessionStatus.ACTIVE
        self.started_at = datetime.now()
        self._events = []

        # Доменное событие: сессия начата
        self._events.append(
            SessionStarted(
                session_id=session_id,
                task_id=task_id,
                user_id=user_id,
                occurred_at=datetime.now()
            )
        )

    @property
    def status(self):
        return self._status

    @property
    def events(self):
        return self._events

    def finish(self):
        if self._status != SessionStatus.ACTIVE:
            raise InvalidSessionStateException("Можно завершить только ACTIVE сессию")

        self._status = SessionStatus.DONE

        # Доменное событие: сессия завершена
        self._events.append(
            SessionCompleted(
                session_id=self.session_id,
                duration_minutes=self.duration.minutes,
                occurred_at=datetime.now()
            )
        )

    def fail(self, reason: str = "Unknown error"):
        self._status = SessionStatus.FAILED

        # Доменное событие: сессия завершилась с ошибкой
        self._events.append(
            SessionFailed(
                session_id=self.session_id,
                reason=reason,
                occurred_at=datetime.now()
            )
        )