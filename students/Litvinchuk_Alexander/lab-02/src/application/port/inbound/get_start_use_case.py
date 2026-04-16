from abc import ABC, abstractmethod

class GetStatsUseCase(ABC):

    @abstractmethod
    def get_stats(self, user_id: str):
        pass