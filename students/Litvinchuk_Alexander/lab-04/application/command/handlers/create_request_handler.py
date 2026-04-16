"""
CreateRequestHandler: Обработчик создания сессии
"""

from application.command.create_request_command import CreateRequestCommand
from domain.models.session import Session
from domain.models.duration import Duration


class CreateRequestHandler:

    def __init__(self, session_repository):
        self.session_repository = session_repository

    def handle(self, command: CreateRequestCommand) -> str:
        # создаём VO
        duration = Duration(command.duration_minutes)

        # создаём агрегат
        session = Session(
            session_id=command.session_id,
            task_id=command.task_id,
            user_id=command.user_id,
            duration=duration
        )

        # сохраняем
        self.session_repository.save(session)

        return session.session_id