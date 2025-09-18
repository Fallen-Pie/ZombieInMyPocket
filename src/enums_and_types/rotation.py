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
