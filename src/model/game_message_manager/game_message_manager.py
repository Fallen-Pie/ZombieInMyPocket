from typing import Any

from ...enums_and_types.game_message import MessageType
from ..interfaces.i_game_message_manager import IGameMessageManager
from enum import Enum

class GameMessageManager(IGameMessageManager):
    """Concrete implementation of IMessageHandler."""

    def __init__(self):
        # Store messages by category
        self._messages: dict[MessageType, list[str]] = {
            MessageType.STATUS: [],
            MessageType.ALERT: [],
            MessageType.FEEDBACK: [],
            MessageType.TOOLTIP: [],
            MessageType.STATISTICS: [],
        }

    def post_message(self, msg_type: MessageType, code: Enum, *args: Any) -> str:
        """Post a new message, formatted from the enum code + args.

        Args:
            msg_type (MessageType): The type of the message.
            code (Enum): The code of the message.
            *args: Arguments to be injected into the message template.
        """
        return msg_type.value.format(*args)

    def get_messages(self, msg_type: MessageType | None = None) -> list[str]:
        """Return a list of formatted messages based on type and enum code."""
        if msg_type:
            return list(self._messages[msg_type])
        return [m for msgs in self._messages.values() for m in msgs]