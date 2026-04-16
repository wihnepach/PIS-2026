from abc import ABC, abstractmethod

class SessionRepository(ABC):

    @abstractmethod
    def save(self, session):
        pass

    @abstractmethod
    def find_active_by_user(self, user_id: str):
        pass