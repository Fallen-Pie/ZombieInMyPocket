# Arsenie: [2] Component for User Story 9 - Status/Notifications/Alerts/Stats
# Used by get_game_message

from abc import ABC, abstractmethod
from enum import Enum
# from typing import Protocol
from ...enums_and_types.game_message import MessageType


class IMessageHandler(ABC):
    """Interface for handling game messages of different types."""

    @abstractmethod
    def post_message(self, msg_type: MessageType, code: Enum, *args) -> None:
        """Post a new message, formatted from the enum code + args.

        Args:
            Message type (MessageType): The type of the message.
            code (Enum): The code of the message.
        """
        pass

    @abstractmethod
    def get_messages(self, msg_type: MessageType | None = None) -> list[str]:
        """Retrieve messages, optionally filtered by type."""
        pass

    @abstractmethod
    def clear_messages(self, msg_type: MessageType | None = None) -> None:
        """Clear all messages or only a specific type."""
        pass


# from abc import ABC, abstractmethod
# from typing import Optional
#
# from . import ITile
# from ...enums_and_types.game_message import GameStateMessage, GameInstruction, AlertMessage,GameOverMessage
#
#
#
#
# #
# class IGameMessageGetter(ABC):
#     """ Handles game status messages."""
#
#     # @abstractmethod
#     # def check_game_state(self) -> GameState:
#     #     pass
#
#     @abstractmethod
#     # TODO: Change condition type to enum of game over conditions
#     def handle_game_over(self, string) -> Optional[GameOverMessage]:
#         """ Game over event-driven that calls appropriate game over message and options, based on GameOverMessage enum"""
#         # TODO: replace the string type with a proper event type
#         pass
#
#     @abstractmethod
#     def get_state_message(self, game_event) -> Optional[GameStateMessage]:
#         """Returns a state update message (e.g., room changed, health update)."""
#         # TODO: replace the string type with a proper event type
#         pass
#
#     @abstractmethod
#     # def get_current_time(self, current_time: ITime) -> int:
#     #     # TODO: use time components to get it.
#     #     pass
#
#     @abstractmethod
#     def handle_help_key(self, current_room: ITile) -> Optional[GameInstruction]:
#         """ Toggles show/hide instruction when H key is pressed, based on GameInstruction enum"""
#         # TODO: replace the string type with a proper event type
#         pass
#
#     @abstractmethod
#     def handle_game_warning_event(self, game_movement, current_tile) -> Optional[AlertMessage]:
#         """ Handles event-driven alerts (e.g. almost time, low health, invalid moves) and informs users based on AlertMessage enum"""
#         # TODO: replace the string type with a proper event type
#         pass
