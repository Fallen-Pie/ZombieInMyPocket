"""Interface definition for game over management in Zombie in My Pocket.

This module defines the abstract base class for handling different game over
conditions and triggering appropriate game end events.
"""

from abc import ABC, abstractmethod
from ..event import Event
from src.enums_and_types import GameOverReason


class IGameOver(ABC):
    """Abstract interface for managing game over conditions.
    
    Handles the different ways the game can end including player death,
    time running out, and successful totem burial.
    """

    @property
    @abstractmethod
    def game_over_event(self) -> Event[GameOverReason]:
        """Get the game over event that can be subscribed to.
        
        Returns:
            Event that fires when the game ends with the reason
        """
        pass

    @game_over_event.setter
    @abstractmethod
    def game_over_event(self, value: Event[GameOverReason]) -> None:
        """Set the game over event.
        
        Args:
            value: The event to set for game over notifications
        """
        pass

    @abstractmethod
    def health_is_zero(self) -> None:
        """Trigger game over due to player health reaching zero.
        
        Called when the player's health drops to 0 or below.
        """
        pass

    @abstractmethod
    def time_is_up(self) -> None:
        """Trigger game over due to time running out.
        
        Called when the game time reaches the limit without completion.
        """
        pass

    @abstractmethod
    def totem_is_buried(self) -> None:
        """Trigger successful game completion by burying the totem.
        
        Called when the player successfully buries the evil totem.
        """
        pass
