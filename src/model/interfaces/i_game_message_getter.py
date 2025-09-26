# Arsenie: [2] Component for User Story 9 - Status/Notifications/Alerts/Stats
# Used by game_message_getter

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
            msg_type (MessageType): The type of the message.
            code (Enum): The code of the message.
        """
        raise NotImplementedError

    @abstractmethod
    def get_messages(self, msg_type: MessageType | None = None) -> list[str]:
        """Retrieve messages, optionally filtered by type."""
        raise NotImplementedError

    @abstractmethod
    def clear_messages(self, msg_type: MessageType | None = None) -> None:
        """Clear all messages or only a specific type."""
        raise NotImplementedError

