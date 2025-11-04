from enum import Enum, auto


class MessageCode(Enum):
    """Codes for all system and status messages in the game."""
    # Scenario 1
    WELCOME = auto()
    # Scenario 2
    ROOM_CHANGED = auto()
    # Scenario 3
    HEALTH_GAINED = auto()
    # Scenario 4.1
    ENTERED_GRAVEYARD = auto()
    # Scenario 4.2
    ENTERED_EVIL_TEMPLE = auto()
    # Scenario 5
    STORAGE_ROOM_PROMPT = auto()
    # Scenario 6
    LOW_HEALTH_WARNING = auto()
    # Scenario 7
    TIME_WARNING = auto()
    # Scenario 8
    ITEM_ACQUIRED = auto()
    # Scenario 10
    ZOMBIE_DOOR_CREATED = auto()
    # Scenario 11
    INVALID_COWER_MOVE = auto()