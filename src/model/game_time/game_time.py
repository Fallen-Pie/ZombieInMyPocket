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

class GameTime(ITime):
    """Handles Game Time and validation"""
    def __init__(self):
        self.time = 9

    def get_current_time(self):
        time_suffix = "pm" if self.time < 12 else "am"
        return f'{self.time}:00{time_suffix}'

    def increase_current_time(self):
        self.time += 1

    def is_time_valid(self):
        return True if self.time < 12 else False