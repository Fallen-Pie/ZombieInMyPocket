# Arsenie: [2] Component for User Story 9 - Status/Notifications/Alerts/Stats
# Used by game_message_manager

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

from ...enums_and_types.game_message import MessageType


class IGameMessageManager(ABC):
    """Interface for handling game messages of different types."""

    def post_message(self, msg_type: MessageType, code: Enum, *args: Any) -> str:
        ...