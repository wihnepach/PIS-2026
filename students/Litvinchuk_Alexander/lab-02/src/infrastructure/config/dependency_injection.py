from infrastructure.adapter.out.in_memory_task_repository import InMemoryTaskRepository
from infrastructure.adapter.out.in_memory_session_repository import InMemorySessionRepository
from infrastructure.adapter.out.in_memory_stats_repository import InMemoryStatsRepository
from infrastructure.adapter.out.mock_notification_service import MockNotificationService

from application.service.task_service import TaskService
from application.service.session_service import SessionService
from application.service.stats_service import StatsService


class DependencyInjectionConfig:

    def __init__(self):
        # Репозитории (исходящие адаптеры)
        self.task_repository = InMemoryTaskRepository()
        self.session_repository = InMemorySessionRepository()
        self.stats_repository = InMemoryStatsRepository()

        # Сервисы уведомлений
        self.notification_service = MockNotificationService()

        # Application Services (входящие порты используют их)
        self.task_service = TaskService(self.task_repository)
        self.session_service = SessionService(
            self.session_repository,
            self.task_repository,
            self.notification_service
        )
        self.stats_service = StatsService(self.stats_repository)

    def get_task_service(self):
        return self.task_service

    def get_session_service(self):
        return self.session_service

    def get_stats_service(self):
        return self.stats_service
