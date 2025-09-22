""" Game Session Manager implementation for the Zombie in My Pocket game.

This module contains the Game Session Manager class and its implementation, handling all session managing functionalities: ...
"""
from ..interfaces.i_game_status import IGameStatus
from ...enums_and_types.game_state import GameState
from ...enums_and_types.game_over_reason import GameOverReason
from ...enums_and_types.enums import GameOverConditions, MessageCode

# from src.enums_and_types.enums import GameState

class GameSessionManager:
    """ Game Session Manager
    Coordinates the state and the components of the game (Time, Turn, Player, and GameOver/GameStatus)
    Coordinates the state and lifecycle of the game session.
    """
    def __init__(self):
        """Initialise a new game session, game state and lifecycle of the game session. Starts game to start state for new game play
        Args:
        """
        self._current_state = GameState.INIT
        self.health = 6  # TODO: replace with actual method/interface that get these values
        self.attack = 1  # TODO: replace with actual method/interface that get these values
        self.room = "Foyer"  # TODO: replace with actual method/interface that get these values

    def set_current_state(self, state:GameState):
        """ Event-driven command that updates game states"""
        if not isinstance(state, GameState):
            raise ValueError("Invalid game state")
        self._current_state = state

    @property
    def get_current_state(self)-> GameState:
        """Gets the current state of the game."""
        return self._current_state


    def start_game(self) -> None:
        """Starts a new game if not already running.

        Args:
            []        
        """
        if self._current_state == GameState.INIT:
            # self._status.reset()
            self._current_state = GameState.EXPLORING
            # self._status.post_message(MessageCode.WELCOME)

    def pause_game(self) -> None:
        """stops all player actions and locks game interactions (e.g. drawing dev cards, moving through tiles, picking items)

        Args:
            []
        """
        if self._current_state == GameState.EXPLORING:
            self._current_state = GameState.PAUSED
            # self._status.post_message(MessageCode.TIME_WARNING)

    def reset_game(self):
        """Completely reset the game session & game values back to init state for new game play.

        Args:
        []
        """
        self.health = 6
        self.attack = 1
        self.room = "Foyer"
        # self._status.reset()
        self._current_state = GameState.INIT

    def resume_game(self) -> None:
        """ []

        Args:
            []
        """
        if self._current_state == GameState.PAUSED:
            self._current_state = GameState.EXPLORING
            # self._status.post_message(MessageCode.ROOM_CHANGED, "Resumed exploring")
    def is_game_over(self):
        """"""
        pass

    def undo_turn(self):
        """Completely reset the game session & game values back to init state for new game play."""
        pass

    def redo_turn(self):
        """Completely reset the game session & game values back to init state for new game play."""
        pass

    def end_game(self, reason: GameOverConditions) -> None:
        """End the game with a win/loss condition. Handles stopping game operations.
        Args:
            []
        """
        self._current_state = GameState.GAME_OVER
        # self._status.trigger_game_over(reason)
        # LOSE: player died, health level run low
        if reason == reason.LOSE_PLAYER_DIED:
            pass
            # self._status.post_message(MessageCode.LOW_HEALTH_WARNING)
        # LOSE: Player ran out of time
        elif reason == GameOverConditions.LOSE_OUT_OF_TIME:
            pass
            # self._status.post_message(MessageCode.TIME_WARNING)
        # WIN: BURIED_TOTEM
        else:
            # self._status.post_message(MessageCode.TIME_WARNING)
            pass

    def stop_game(self):
        """"""
        pass

    def victory(self) -> None:
        """ []

        Args:
            []
        """
        self._current_state = GameState.VICTORY
        # self._status.trigger_game_over(GameOverConditions.WIN_TOTEM_BURIED)
        # self._status.post_message(MessageCode.ENTERED_EVIL_TEMPLE)

    def save_game(self):
        """ Save game progress """
        pass

    def get_snapshot(self):
        """ Return game snapshot """
        pass

    def load_game(self):
        """ Restore saved game progress """
        pass