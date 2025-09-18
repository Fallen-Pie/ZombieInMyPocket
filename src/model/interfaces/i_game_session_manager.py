# Arsenie: [1] Component for User Story 12 - Game set-up start thing
# Used by game_session_manager

from abc import abstractmethod, ABC

from ...enums_and_types import GameState

class IGameStateManager(ABC):
    """Interface for win/loss outcomes. Also known as IWinLossHandler"""
    @abstractmethod
    def set_current_state(self) -> GameState:
        pass

    @abstractmethod
    def reset_game(self):
        """Resets game to start state for new game play"""
        pass

    @abstractmethod
    def stop_game(self):
        """stops all player actions and locks game interactions (e.g. drawing dev cards, moving through tiles, picking items)"""
        pass
