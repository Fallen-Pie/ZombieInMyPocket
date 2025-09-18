from enum import Enum

class Direction(Enum):
    """Direction of where doors are and where the player can move to."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
