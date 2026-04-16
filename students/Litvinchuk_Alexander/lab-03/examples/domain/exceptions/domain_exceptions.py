"""
Domain Exceptions: Доменные исключения для Pomodoro Session

Исключения для бизнес-логики Pomodoro-сессий
Предметная область: Томатная продуктивность
"""


class DomainException(Exception):
    """Базовый класс для доменных исключений"""
    pass


class InvalidSessionStateException(DomainException):
    """Исключение: Недопустимое состояние Pomodoro-сессии"""
    pass