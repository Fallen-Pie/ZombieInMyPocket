from enum import Enum, auto
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    pass


class Rotation(Enum):
    """Rotation of a tile."""

    NONE = 0
    """No rotation."""

    CLOCKWISE = 1
    """Rotated 90 degrees clockwise."""

    UPSIDE_DOWN = 2
    """Rotated 180 degrees"""

    ANTICLOCKWISE = 3
    """Rotated 90 degrees anticlockwise."""


class Direction(Enum):
    """Direction of where doors are and where the player can move to."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Input_options(Enum):
    """Input_options yes or no."""

    YES = 0
    NO = 1


class ItemType(Enum):
    WEAPON = 0
    HEALING = 1  # Can of Soda
    COMBINE_ONLY = 2  # Candle and Gasoline
    ESCAPE = 3  # Using oil by itself without combining it

class ItemInfo(Enum):
    SPADE = ("Spade", "A sturdy digging tool that can be used as a weapon", ItemType.WEAPON, 2, 0, False, cast(list['ItemInfo'], []))
    AXE = ("Axe", "A sharp wood-cutting axe effective in combat", ItemType.WEAPON, 3, 0, False, cast(list['ItemInfo'], []))
    BANDAGE = ("Bandage", "Basic medical supplies for treating wounds", ItemType.HEALING, 0, 3, True, cast(list['ItemInfo'], []))
    HEALTH_KIT = ("Health Kit", "Advanced medical kit for serious injuries", ItemType.HEALING, 0, 8, True, cast(list['ItemInfo'], []))
    
    def __init__(self, display_name: str, description: str, item_type: ItemType, 
                 attack_bonus: int, heal_amount: int, is_single_use: bool, 
                 combinable_with: list['ItemInfo']):
        self.display_name = display_name
        self.description = description
        self.item_type = item_type
        self.attack_bonus = attack_bonus
        self.heal_amount = heal_amount
        self.is_single_use = is_single_use
        self.combinable_with = combinable_with

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


class GameOverConditions(Enum):
    WIN_TOTEM_BURIED = auto()
    LOSE_PLAYER_DIED = auto()
    LOSE_OUT_OF_TIME = auto()

class ItemName(Enum):
    OIL = "Oil"
    GASOLINE = "Gasoline"
    BOARD_WITH_NAILS = "Board With Nails"
    CAN_OF_SODA = "Can of Soda"
    GRISLY_FEMUR = "Grisly Femur"
    GOLF_CLUB = "Golf Club"
    CANDLE = "Candle"
    CHAINSAW = "Chainsaw"
    MACHETE = "Machete"
