# Arsenie: [2] Component for User Story 9 - Status/Notifications/Alerts/Stats
# Used by game_message_manager

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

# from typing import Protocol
from ...enums_and_types.game_message import MessageType


class IGameMessageManager(ABC):
    """Interface for handling game messages of different types."""

    def post_message(self, msg_type: MessageType, code: Enum, *args: Any) -> str:
        ...

    # @abstractmethod
    # def post_message(self, msg_type: MessageType, code: Enum, *args) -> str:
    #     """Post a new message, formatted from the enum code + args.
    #
    #     Args:
    #         msg_type (MessageType): The type of the message.
    #         code (Enum): The code of the message.
    #         *args: Arguments to be injected into the message template.
    #     """
    #     try:
    #         formatted_code_msg = code.value.format(*args)
    #     except (IndexError, KeyError):
    #         # Fallback if no placeholders exist in code.value
    #         formatted_code_msg = code.value
    #
    #     try:
    #         final_msg = msg_type.value.format(formatted_code_msg)
    #     except (IndexError, KeyError):
    #         # Some msg_types like STATISTICS expect multiple args
    #         final_msg = msg_type.value.format(*args)
    #
    #     return final_msg
