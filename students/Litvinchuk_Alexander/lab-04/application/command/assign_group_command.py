"""
AssignGroupCommand: Команда изменения состояния сессии (например завершение)
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AssignGroupCommand:
    """
    Команда: изменить состояние сессии

    Поля:
    - session_id: ID сессии
    - action: действие (finish / fail)
    - reason: причина (для fail)
    """
    session_id: str
    action: str
    reason: str | None = None

    def __post_init__(self):
        if not self.session_id:
            raise ValueError("session_id обязателен")

        if self.action not in ["finish", "fail"]:
            raise ValueError("action должен быть 'finish' или 'fail'")