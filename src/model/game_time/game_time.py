from src.common import ITime

class GameTime(ITime):
    """Handles Game Time and validation"""
    START_TIME = 9
    END_TIME = 12
    TIME_INCREMENT = 1

    def __init__(self):
        self.time = self.START_TIME

    def get_current_time(self) -> int:
        return self.time

    def increase_current_time(self):
        self.time += self.TIME_INCREMENT

    def is_time_valid(self) -> bool:
        return True if self.time < self.END_TIME else False