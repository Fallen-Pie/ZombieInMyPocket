from abc import ABC, abstractmethod

class ITime(ABC):
    """Abstract Class for building GameTime Classes"""
    @abstractmethod
    def get_current_time(self):
        ...

    @abstractmethod
    def increase_current_time(self):
        ...

    @abstractmethod
    def is_time_valid(self):
        ...