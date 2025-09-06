from enum import Enum

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
