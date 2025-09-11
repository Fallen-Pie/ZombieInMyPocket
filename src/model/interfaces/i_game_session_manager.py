from abc import ABC, abstractmethod
from src.enums_and_types.enums import GameState

class IGameSessionManager(ABC):
    """ """

    @abstractmethod
    def set_current_state(self) -> bool:
        """"""
        pass

    @abstractmethod
    def get_current_state(self) -> GameState:
        """"""
        pass

    @abstractmethod
    def setup_game(self) -> None:
        """"""
        pass

    def start_game(self) -> None:
        """"""
        pass

    def end_game(self) -> None:
        """"""
        pass




