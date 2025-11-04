"""Interface definition for development cards in Zombie in My Pocket.

This module defines the abstract base class for development cards that
contain items and encounter information based on the game time.
"""

from abc import ABC, abstractmethod
from .i_encounter import IEncounter
from .i_item import IItem


class IDevCard(ABC):
    """Abstract interface for development cards in the game.
    
    Development cards contain an item and encounters that vary based on
    the current time of day in the game.
    """

    @abstractmethod
    def get_item(self) -> IItem:
        """Get the item contained on this development card.
        
        Returns:
            The item found on this card
        """
        pass

    @abstractmethod
    def get_encounter(self, time: int) -> IEncounter:
        """Get the encounter for this card based on the current time.
        
        Args:
            time: Current game time (affects which encounter occurs)
            
        Returns:
            The encounter appropriate for the given time
        """
        pass
