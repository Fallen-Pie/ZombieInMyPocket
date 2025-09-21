

class GameTime:
    """Keeps track of game time"""
    _AM = 'AM'
    _PM = 'PM'

    _INCREMENT = 1
    _TIME_DISPLAY_PREFIX = "The time is now "
    _TIME_DISPLAY_INFIX = ":00"


    def __init__(self, start_time: int = 9, end_time: int = 12):
        self._time: int = start_time
        self._start_time: int = start_time
        self._end_time: int = end_time


    def __str__(self) -> str:
        """returns the current hour as a string"""
        return f"{self._TIME_DISPLAY_PREFIX}{self._time:02d}{self._TIME_DISPLAY_INFIX}{self._get_am_pm()}"


    def get_current_time(self) -> int:
        """returns the current hour as a number"""
        return self._time


    def increase_time(self) -> None:
        """Increases the time by one hour"""
        self._time += self._INCREMENT


    def is_time_valid(self) -> bool:
        """returns True if the current time is between 9 and 12"""
        return self._start_time <= self._time < self._end_time


    def _get_am_pm(self):
        """
        returns the AM/PM time as a string
        I think, therefore I am or pm
        """
        if self._is_am():
            return self._AM
        else:
            return self._PM


    def _is_am(self):
        """returns True if the current time is 12"""
        return self._time == 12