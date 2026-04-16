from abc import ABC, abstractmethod

class TaskRepository(ABC):

    @abstractmethod
    def find_by_id(self, task_id: str):
        pass