"""Interface definition for encounters in Zombie in My Pocket.

This module defines the abstract base class for encounters that can occur
when the player enters certain tiles or draws development cards.
"""

from abc import ABC, abstractmethod


class IEncounter(ABC):
    """Abstract interface for game encounters.
    
    Encounters represent events that occur during gameplay such as
    combat with zombies, finding items, or other special events.
    """
    
    @abstractmethod
    def set_values(self, value):
        """Set the parameters for this encounter.
        
        Args:
            value: The configuration data for this encounter
        """
        ...

    @abstractmethod
    def handle_encounter(self, player):
        """Execute the encounter with the given player.
        
        Args:
            player: The player object that triggered the encounter
        """
        ...
