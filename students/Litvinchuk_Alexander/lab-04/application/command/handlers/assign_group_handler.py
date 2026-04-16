"""
AssignGroupHandler: Обработчик изменения состояния сессии
"""

from application.command.assign_group_command import AssignGroupCommand


class AssignGroupHandler:

    def __init__(self, session_repository):
        self.session_repository = session_repository

    def handle(self, command: AssignGroupCommand):
        # 1. получаем сессию
        session = self.session_repository.find_by_id(command.session_id)

        if not session:
            raise ValueError("Session не найдена")

        # 2. выполняем действие
        if command.action == "finish":
            session.finish()

        elif command.action == "fail":
            session.fail(command.reason or "error")

        # 3. сохраняем
        self.session_repository.save(session)