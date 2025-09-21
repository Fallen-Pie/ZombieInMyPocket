"""Base classes for game items in Zombie in My Pocket.

This module defines the base item classes that implement the IItem interface
and provide common functionality for different types of items in the game.
"""

from typing import Optional
from src.enums_and_types import ItemName, ItemType
from ..interfaces import IItem


class BaseItem(IItem):
    """Base implementation of a game item.
    
    Provides common functionality for all items including name, description,
    type, combat bonuses, healing amounts, and usage tracking.
    """
    def __init__(self, name: ItemName, description: str, item_type: ItemType,
                 attack_bonus: int = 0, heal_amount: int = 0,
                 uses: int = 1,
                 combinable_with: Optional[list[ItemName]] = None) -> None:
        """Initialize a base item.
        
        Args:
            name: The unique identifier for this item
            description: Human-readable description of the item
            item_type: The category this item belongs to
            attack_bonus: Combat bonus this item provides (default: 0)
            heal_amount: Health points this item restores (default: 0)
            uses: Number of times this item can be used (default: 1)
            combinable_with: List of items this can combine with (default: [])
        """
        self._name = name
        self._description = description
        self._type = item_type
        self._attack_bonus = attack_bonus
        self._heal_amount = heal_amount
        self._max_uses = uses
        self._uses_remaining = uses
        self._combinable_with = combinable_with or []

    @property
    def name(self) -> ItemName:
        """Get the item's unique name identifier."""
        return self._name

    @property
    def description(self) -> str:
        """Get the item's description text."""
        return self._description

    @property
    def type(self) -> ItemType:
        """Get the item's type category."""
        return self._type

    @property
    def attack_bonus(self) -> int:
        """Get the combat bonus this item provides."""
        return self._attack_bonus

    @property
    def heal_amount(self) -> int:
        """Get the health points this item restores when used."""
        return self._heal_amount

    @property
    def uses_remaining(self) -> int:
        """Get the number of uses left for this item."""
        return self._uses_remaining

    @property
    def combinable_with(self) -> list[ItemName]:
        """Get a copy of the list of items this can combine with."""
        return self._combinable_with.copy()

    def use(self) -> bool:
        """Use the item, decrementing its remaining uses.
        
        Returns:
            True if the item is fully consumed after use, False otherwise
        """
        if self._uses_remaining <= 0:
            return True

        self._uses_remaining -= 1
        return self._uses_remaining <= 0


class ConsumableItem(BaseItem):
    """An item that can be consumed for healing effects.
    
    Consumable items are single-use items that restore health points.
    """
    def __init__(self, name: ItemName, description: str, item_type: ItemType,
                 heal_amount: int = 0,
                 combinable_with: Optional[list[ItemName]] = None) -> None:
        """Initialize a consumable item.
        
        Args:
            name: The unique identifier for this item
            description: Human-readable description of the item
            item_type: The category this item belongs to
            heal_amount: Health points this item restores (default: 0)
            combinable_with: List of items this can combine with (default: [])
        """
        super().__init__(name, description, item_type,
                         heal_amount=heal_amount, uses=1,
                         combinable_with=combinable_with)


class WeaponItem(BaseItem):
    """An item that provides combat bonuses.
    
    Weapon items increase the player's attack score and typically have
    multiple uses before being consumed.
    """
    def __init__(self, name: ItemName, description: str, attack_bonus: int,
                 uses: int = 99,
                 combinable_with: Optional[list[ItemName]] = None) -> None:
        """Initialize a weapon item.
        
        Args:
            name: The unique identifier for this item
            description: Human-readable description of the item
            attack_bonus: Combat bonus this weapon provides
            uses: Number of times this weapon can be used (default: 99)
            combinable_with: List of items this can combine with (default: [])
        """
        super().__init__(name, description, ItemType.WEAPON,
                         attack_bonus=attack_bonus, uses=uses,
                         combinable_with=combinable_with)


class CombinableItem(BaseItem):
    """An item that exists primarily to be combined with other items.
    
    These items have limited functionality on their own but can create
    powerful effects when combined with compatible items.
    """
    def __init__(self, name: ItemName, description: str, item_type: ItemType,
                 combinable_with: list[ItemName]) -> None:
        """Initialize a combinable item.
        
        Args:
            name: The unique identifier for this item
            description: Human-readable description of the item
            item_type: The category this item belongs to
            combinable_with: List of items this can combine with
        """
        super().__init__(name, description, item_type, uses=1,
                         combinable_with=combinable_with)


class SpecialWeaponItem(WeaponItem):
    """A weapon item with special capabilities like refuelable uses.
    
    Special weapons can have their uses replenished through combinations
    with other items, unlike regular weapons.
    """
    def add_uses(self, amount: int) -> None:
        """Add additional uses to this special weapon.
        
        Args:
            amount: Number of uses to add
        """
        self._uses_remaining += amount
