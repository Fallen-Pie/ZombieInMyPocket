"""Factory for creating game items in Zombie in My Pocket.

This module provides the factory pattern implementation for creating
different types of items based on their configuration data. It handles
the instantiation of the correct item subclass based on item type.
"""

from src.enums_and_types import ItemName, ItemType
from ..interfaces import IItem
from .base_item import (ConsumableItem, WeaponItem, CombinableItem,
                        SpecialWeaponItem)
from .item_config import ITEM_CONFIGS


class ItemFactory:
    """Factory class for creating game items from configuration data.
    
    Uses the factory pattern to instantiate the appropriate item subclass
    based on the item's type and configuration.
    """
    @staticmethod
    def create_item(name: ItemName) -> IItem:
        """Create an item instance from its name.
        
        Args:
            name: The unique identifier of the item to create
            
        Returns:
            An instance of the appropriate item subclass
            
        Raises:
            ValueError: If the item name is unknown or item type is unsupported
        """
        if name not in ITEM_CONFIGS:
            raise ValueError(f"Unknown item: {name}")

        config = ITEM_CONFIGS[name]

        if config.item_type == ItemType.HEALING:
            return ConsumableItem(
                name=config.name,
                description=config.description,
                item_type=config.item_type,
                heal_amount=config.heal_amount,
                combinable_with=config.combinable_with
            )

        elif config.item_type == ItemType.WEAPON:
            if name == ItemName.CHAINSAW:
                return SpecialWeaponItem(
                    name=config.name,
                    description=config.description,
                    attack_bonus=config.attack_bonus,
                    uses=config.uses,
                    combinable_with=config.combinable_with
                )
            else:
                return WeaponItem(
                    name=config.name,
                    description=config.description,
                    attack_bonus=config.attack_bonus,
                    uses=config.uses,
                    combinable_with=config.combinable_with
                )

        elif config.item_type in [ItemType.COMBINE_ONLY, ItemType.ESCAPE]:
            return CombinableItem(
                name=config.name,
                description=config.description,
                item_type=config.item_type,
                combinable_with=config.combinable_with
            )

        else:
            raise ValueError(f"Unsupported item type: {config.item_type}")


def get_item(name: ItemName) -> IItem:
    """Convenience function to create an item by name.
    
    Args:
        name: The unique identifier of the item to create
        
    Returns:
        An instance of the appropriate item subclass
    """
    return ItemFactory.create_item(name)


def get_all_items() -> list[IItem]:
    """Returns a list of all available items in the game.
    
    Returns:
        List containing one instance of each item type in the game
    """
    return [get_item(item_name) for item_name in ItemName]
