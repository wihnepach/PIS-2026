"""
Domain Events: События для Pomodoro Session

Доменные события регистрируются при изменении состояния Pomodoro-сессии
Предметная область: Томатная продуктивность
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SessionStarted:
    """Событие: Сессия начата"""
    session_id: str
    task_id: str
    user_id: str
    occurred_at: datetime


@dataclass(frozen=True)
class SessionPaused:
    """Событие: Сессия поставлена на паузу"""
    session_id: str
    occurred_at: datetime


@dataclass(frozen=True)
class SessionResumed:
    """Событие: Сессия продолжена"""
    session_id: str
    occurred_at: datetime


@dataclass(frozen=True)
class SessionCompleted:
    """Событие: Сессия успешно завершена"""
    session_id: str
    duration_minutes: int
    occurred_at: datetime


@dataclass(frozen=True)
class SessionFailed:
    """Событие: Сессия завершилась с ошибкой"""
    session_id: str
    reason: str
    occurred_at: datetime