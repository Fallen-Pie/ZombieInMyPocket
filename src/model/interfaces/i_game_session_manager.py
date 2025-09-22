# Arsenie: [1] Component for User Story 12 - Game set-up start thing
# Used by game_session_manager

from abc import abstractmethod, ABC
from ...enums_and_types.game_state import GameState
from ...enums_and_types.enums import GameOverConditions

class IGameSessionManager(ABC):
    """Interface for all game states and win/loss outcomes for the session, which includes IWinLossHandler"""
    @abstractmethod
    def set_current_state(self):
        pass

    @abstractmethod
    def get_current_state(self) -> GameState:
        """Gets the current state of the game."""
        pass

    @abstractmethod
    def start_game(self):
        """Starts a new game if not already running."""
        pass

    @abstractmethod
    def pause_game(self):
        """stops all player actions and locks game interactions (e.g. drawing dev cards, moving through tiles, picking items)"""
        pass

    @abstractmethod
    def reset_game(self):
        """Completely reset the game session & game values back to init state for new game play."""
        pass

    def resume_game(self):
        """"""
        pass

    def is_game_over(self):
        """"""
        pass

    @abstractmethod
    def undo_turn(self):
        """Completely reset the game session & game values back to init state for new game play."""
        pass

    @abstractmethod
    def redo_turn(self):
        """Completely reset the game session & game values back to init state for new game play."""
        pass

    def end_game(self, reason: GameOverConditions):
        """"""
        pass

    @abstractmethod
    def stop_game(self):
        """stops all player actions and locks game interactions (e.g. drawing dev cards, moving through tiles, picking items)"""
        pass
    def victory(self) -> None:
        """"""

    def save_game(self):
        """ Save game progress """
        pass

    def get_snapshot(self):
        """ Return game snapshot """
        pass

    def load_game(self):
        """ Restore saved game progress """
        pass