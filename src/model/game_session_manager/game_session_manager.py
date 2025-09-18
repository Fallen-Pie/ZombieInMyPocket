""" Game Session Manager implementation for the Zombie in My Pocket game.

This module contains the Game Session Manager class and its implementation, handling all session managing functionalities: ... 
"""
from ..interfaces.i_game_status import IGameStatus
from ...enums_and_types.game_state import GameState
from ...enums_and_types.game_over_condition import GameOverConditions
from ...enums_and_types.message_code import MessageCode

class GameSessionManager:
    """ Game Session Manager 
    
    """
    """Coordinates the state and lifecycle of the game session."""
    def __init__(self, status: IGameStatus):
        """Initialise a new game session. 
        
        Args: 
        """
        self._status = status
        self._state = GameState.INIT

    @property
    def state(self) -> GameState:
        """ []

        Args:
            []
        """
        return self._state

    def start_game(self) -> None:
        """Start a new game if not already running.

        Args:
            []        
        """
        if self._state == GameState.INIT:
            self._status.reset()
            self._state = GameState.EXPLORING
            self._status.post_message(MessageCode.WELCOME)

    def pause(self) -> None:
        """ []

        Args:
            []
        """        
        if self._state == GameState.EXPLORING:
            self._state = GameState.PAUSED
            self._status.post_message(MessageCode.TIME_WARNING)

    def resume(self) -> None:
        """ []

        Args:
            []
        """        
        if self._state == GameState.PAUSED:
            self._state = GameState.EXPLORING
            self._status.post_message(MessageCode.ROOM_CHANGED, "Resumed exploring")

    def reset(self) -> None:
        """Completely reset the session back to init state.

        Args:
            []
        """
        self._status.reset()
        self._state = GameState.INIT

    def end_game(self, condition: GameOverConditions) -> None:
        """End the game with a win/loss condition.

        Args:
            []        
        """
        self._state = GameState.GAME_OVER
        self._status.trigger_game_over(condition)
        # You can add a message here too if needed:
        if condition == GameOverConditions.LOSE_PLAYER_DIED:
            self._status.post_message(MessageCode.LOW_HEALTH_WARNING)
        elif condition == GameOverConditions.LOSE_OUT_OF_TIME:
            self._status.post_message(MessageCode.TIME_WARNING)

    def victory(self) -> None:
        """ []

        Args:
            []
        """         
        self._state = GameState.VICTORY
        self._status.trigger_game_over(GameOverConditions.WIN_TOTEM_BURIED)
        self._status.post_message(MessageCode.ENTERED_EVIL_TEMPLE)
