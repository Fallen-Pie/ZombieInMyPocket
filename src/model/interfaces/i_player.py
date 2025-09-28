"""Interface definition for the player in Zombie in My Pocket.

This module defines the abstract base class that represents the player character,
specifying required methods for health management, combat, movement, and inventory.
"""

from abc import ABC, abstractmethod
from src.enums_and_types.types import Position
from .i_item import IItem


class IPlayer(ABC):
    """Abstract interface defining the contract for player objects in the game.
    
    The player interface defines all the essential player actions including
    health management, combat mechanics, movement, inventory management,
    and item usage including combinations.
    """

    @abstractmethod
    def get_health(self) -> int:
        """Get the player's current health points.
        
        Returns:
            Current health as an integer
        """
        pass

    @abstractmethod
    def take_damage(self, amount: int) -> None:
        """Reduce the player's health by the specified amount.
        
        Args:
            amount: Number of health points to remove
        """
        pass

    @abstractmethod
    def heal(self, amount: int) -> None:
        """Increase the player's health by the specified amount.
        
        Args:
            amount: Number of health points to restore
        """
        pass

    @abstractmethod
    def get_attack_power(self) -> int:
        """Get the player's total attack power including item bonuses.
        
        Returns:
            Total attack value including base stats and equipped item bonuses
        """
        pass

    @abstractmethod
    def has_totem(self) -> bool:
        """Check if the player possesses the evil totem.
        
        Returns:
            True if the player has the totem, False otherwise
        """
        pass

    def set_has_totem(self, has_totem: bool) -> None:
        """Set the totem possession state.
        
        Args:
            has_totem: True if player should have the totem, False otherwise
        """
        pass

    @abstractmethod
    def get_position(self) -> Position:
        """Get the player's current position on the game board.
        
        Returns:
            The player's current Position coordinates
        """
        pass

    @abstractmethod
    def set_position(self, position: Position) -> None:
        """Move the player to a new position on the game board.
        
        Args:
            position: The new Position coordinates for the player
        """
        pass

    @abstractmethod
    def use_item(self, item: IItem) -> None:
        """Use an item from the player's inventory.
        
        Args:
            item: The item to use from inventory
        """
        pass

    @abstractmethod
    def get_inventory(self) -> list[IItem]:
        """Get a copy of the player's current inventory.
        
        Returns:
            List of items currently in the player's possession
        """
        pass

    @abstractmethod
    def add_item_to_inventory(self, item: IItem) -> None:
        """Add an item to the player's inventory.
        
        Args:
            item: The item to add to inventory
        """
        pass

    @abstractmethod
    def remove_item_from_inventory(self, item: IItem) -> None:
        """Remove an item from the player's inventory.
        
        Args:
            item: The item to remove from inventory
        """
        pass

    @abstractmethod
    def combine_items_from_inventory(self) -> bool:
        """Attempt to combine compatible items in the inventory.
        
        Returns:
            True if a combination was successful, False otherwise
        """
        pass
