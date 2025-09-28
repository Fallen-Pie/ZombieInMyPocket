"""Interface definition for game items in Zombie in My Pocket.

This module defines the abstract base class that all game items must implement,
specifying the required properties and methods for item functionality.
"""

from abc import ABC, abstractmethod
from src.enums_and_types import *


class IItem(ABC):
    """Abstract interface defining the contract for item objects in the game.
    
    All items in the game must implement this interface to provide consistent
    access to item properties like name, description, combat effects, healing
    amounts, usage limits, and combination capabilities.
    """

    @property
    @abstractmethod
    def name(self) -> ItemName:
        """Get the unique identifier for this item.
        
        Returns:
            The item's unique name from the ItemName enum
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Get the human-readable description of the item.
        
        Returns:
            A string describing the item's effects and usage
        """
        pass

    @property
    @abstractmethod
    def type(self) -> ItemType:
        """Get the category this item belongs to.
        
        Returns:
            The item's type from the ItemType enum (WEAPON, HEALING, etc.)
        """
        pass

    @property
    @abstractmethod
    def attack_bonus(self) -> int:
        """Get the combat bonus this item provides.
        
        Returns:
            Integer value added to the player's attack score (0 for non-weapons)
        """
        pass

    @property
    @abstractmethod
    def heal_amount(self) -> int:
        """Get the health points this item restores when used.
        
        Returns:
            Integer health points restored (0 for non-healing items)
        """
        pass

    # @property
    # @abstractmethod
    # def is_single_use(self) -> bool:
    #     pass

    # Changed is_single_use to uses_remaning because the chainsaw
    # has multiple uses
    @property
    @abstractmethod
    def uses_remaining(self) -> int:
        """Number of uses remaining."""
        pass

    @property
    @abstractmethod
    def combinable_with(self) -> list[ItemName]:
        """Get the list of items this can be combined with.
        
        Returns:
            List of ItemName values that this item can combine with
        """
        pass

    @abstractmethod
    def use(self) -> bool:
        """Use the item, decrementing its remaining uses.
        
        This method handles the consumption of the item when used,
        decreasing the uses_remaining counter for limited-use items.
        
        Returns:
            True if the item is fully consumed after use, False otherwise
        """
        pass
