from abc import ABC, abstractmethod
from typing import Optional

from . import ITile
from ...enums_and_types.enums import GameStateMessage, GameInstruction, AlertMessage, UnknownErrorMessage, GameState, \
    GameOverMessage

class IGameStatus(ABC):
    """ Handles game status messages."""

    # @abstractmethod
    # def check_game_state(self) -> GameState:
    #     pass

    @abstractmethod
    # TODO: Change condition type to enum of game over conditions
    def handle_game_over(self, string) -> Optional[GameOverMessage]:
        """ Game over event-driven that calls appropriate game over message and options, based on GameOverMessage enum"""
        # TODO: replace the string type with a proper event type
        pass

    @abstractmethod
    def get_current_time(self) -> int:
        # TODO: use time components to get it.
        pass

    @abstractmethod
    def get_state_message(self, string) -> Optional[GameStateMessage]:
        """Returns a state update message (e.g., room changed, health update)."""
        # TODO: replace the string type with a proper event type
        pass

    @abstractmethod
    def handle_help_key(self, current_room: ITile.get_name()) -> Optional[GameInstruction]:
        """ Toggles show/hide instruction when H key is pressed, based on GameInstruction enum"""
        # TODO: replace the string type with a proper event type
        pass

    @abstractmethod
    def handle_game_warning_event(self) -> Optional[AlertMessage]:
        """ Handles event-driven alerts (e.g. almost time, low health, invalid moves) and informs users based on AlertMessage enum"""
        # TODO: replace the string type with a proper event type
        pass
