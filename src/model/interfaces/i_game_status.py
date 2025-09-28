from abc import ABC, abstractmethod
from ...enums_and_types.enums import MessageCode, GameOverConditions


class IGameStatus(ABC):
    """
    An interface to handle game state changes and construct status messages.
    """

    @property
    @abstractmethod
    def is_game_over(self) -> bool:
        pass

    @property
    @abstractmethod
    def game_over_condition(self) -> GameOverConditions | None:
        pass

    @abstractmethod
    def get_messages(self) -> list[str]:
        pass

    @abstractmethod
    def clear_messages(self) -> None:
        pass

    @abstractmethod
    def post_message(self, code: MessageCode, *args) -> None:
        pass

    @abstractmethod
    def trigger_game_over(self, condition: GameOverConditions) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass
