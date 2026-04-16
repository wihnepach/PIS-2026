"""
CreateRequestCommand: Команда создания Pomodoro-сессии (Request)
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CreateRequestCommand:
    """
    Команда: создать новую сессию (Request)

    Поля:
    - session_id: ID сессии
    - task_id: ID задачи
    - user_id: ID пользователя
    - duration_minutes: длительность
    """
    session_id: str
    task_id: str
    user_id: str
    duration_minutes: int

    def __post_init__(self):
        if not self.session_id:
            raise ValueError("session_id обязателен")
        if not self.task_id:
            raise ValueError("task_id обязателен")
        if not self.user_id:
            raise ValueError("user_id обязателен")
        if self.duration_minutes <= 0:
            raise ValueError("duration_minutes должен быть > 0")