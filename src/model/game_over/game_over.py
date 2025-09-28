from ..event import Event
from src.enums_and_types import GameOverReason
from ..interfaces import IGameOver


class GameOver(IGameOver):

    def __init__(self) -> None:
        self.__game_over_event = Event[GameOverReason]()

    @property
    def game_over_event(self) -> Event[GameOverReason]:
        return self.__game_over_event

    @game_over_event.setter
    def game_over_event(self, value: Event[GameOverReason]) -> None:
        self.__game_over_event = value

    def health_is_zero(self) -> None:
        self.__game_over_event(GameOverReason.HEALTH)

    def time_is_up(self) -> None:
        self.__game_over_event(GameOverReason.OUT_OF_TIME)

    def totem_is_buried(self) -> None:
        self.__game_over_event(GameOverReason.BURIED_TOTEM)
