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
            MessageType.INVALID_MOVE: [],
            MessageType.TOOLTIP: [],
            MessageType.STATISTICS: [],
        }
    @staticmethod
    def _format(code: Enum, *args) -> str:
        """Publish a formatted message based on type and enum code.
        :rtype: str
        """
        template = code.value

        exception_map = {
            IndexError: "not enough positional arguments",
            KeyError: "missing named argument",
            ValueError: "invalid format string",
            AttributeError: "template is not a string",
        }

        try:
            return code.value.format(*args)
        except tuple(exception_map.keys()) as e:
            raise ValueError(f"Formatting error for {code.name}: {e}")

    def post_message(self, msg_type: MessageType, code: Enum, *args) -> None:
        """Post a new message, formatted from the enum code + args.

        Args:
            msg_type (MessageType): The type of the message.
            code (Enum): The code of the message.
            *args: Arguments to be injected into the message template.
        """

        message = self._format(code, *args)
        self._messages[msg_type].append(message)

    def get_messages(self, msg_type: MessageType | None = None) -> list[str]:
        """Return a list of formatted messages based on type and enum code."""
        if msg_type:
            return list(self._messages[msg_type])
        return [m for msgs in self._messages.values() for m in msgs]

#     def clear_messages(self, msg_type: MessageType | None = None) -> None:
#         """Clear all messages based on type and enum code."""
#         if msg_type:
#             self._messages[msg_type].clear()
#         else:
#             for msgs in self._messages.values():
#                 msgs.clear()
