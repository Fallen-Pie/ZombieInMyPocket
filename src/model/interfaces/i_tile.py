"""Interface definition for game tiles in Zombie in My Pocket.

This module defines the abstract base class for tiles that make up the
game board, including their exits, encounters, and special properties.
"""

from abc import ABC, abstractmethod
from src.enums_and_types import *
from ..encounters.encounters import IEncounter


class ITile(ABC):
    """Abstract interface for game tiles.
    
    Tiles represent rooms and outdoor areas that the player can explore.
    Each tile has exits, may contain encounters, and can be rotated.
    """

    @abstractmethod
    def get_name(self) -> str:
        """Get the name of this tile.
        
        Returns:
            The tile's descriptive name
        """
        pass

    @abstractmethod
    def is_outdoors(self) -> bool:
        """Check if this tile represents an outdoor area.
        
        Returns:
            True if this is an outdoor tile, False for indoor
        """
        pass

    @abstractmethod
    def get_exits(self) -> tuple[Direction, ...]:
        """Get the exit directions for this tile based on its current rotation.
        
        Returns:
            Tuple of Direction values indicating where exits are located
        """
        pass

    @abstractmethod
    def get_front_door(self) -> Direction | None:
        """Get the direction to the front door if this tile has one.
        
        Only certain tiles (like patio and dining room) have front doors.
        
        Returns:
            Direction to the front door, or None if this tile has no front door
        """
        pass

    @abstractmethod
    def get_encounter(self) -> IEncounter | None:
        """Get the encounter associated with this tile.
        
        Returns:
            The encounter for this tile, or None if no encounter exists
        """
        pass

    @abstractmethod
    def set_rotation(self, rotation: Rotation) -> None:
        """Set the rotation of this tile.
        
        Args:
            rotation: The new rotation to apply to the tile
        """
        pass
