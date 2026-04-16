from abc import ABC, abstractmethod

class StartSessionUseCase(ABC):

    @abstractmethod
    def start(self, task_id: str, user_id: str):
        pass