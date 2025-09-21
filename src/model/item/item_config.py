"""Configuration data for game items in Zombie in My Pocket.

This module contains the configuration definitions for all game items,
including their properties like attack bonuses, healing amounts, usage limits,
and combination rules.
"""

from dataclasses import dataclass
from typing import Optional
from src.enums_and_types import ItemName, ItemType


@dataclass
class ItemConfig:
    """Configuration data for a game item.
    
    Attributes:
        name: Unique identifier for the item
        description: Human-readable description of the item's effects
        item_type: Category this item belongs to
        attack_bonus: Combat bonus this item provides (default: 0)
        heal_amount: Health points this item restores (default: 0)
        uses: Number of times this item can be used (default: 1)
        combinable_with: List of items this can combine with (default: [])
    """
    name: ItemName
    description: str
    item_type: ItemType
    attack_bonus: int = 0
    heal_amount: int = 0
    uses: int = 1
    combinable_with: Optional[list[ItemName]] = None

    def __post_init__(self):
        """Initialize combinable_with to empty list if None."""
        if self.combinable_with is None:
            self.combinable_with = []


# Dictionary mapping item names to their configuration data
ITEM_CONFIGS = {
    ItemName.OIL: ItemConfig(
        name=ItemName.OIL,
        description=("Throw as you run away to avoid taking damage. "
                     "Combine with Candle to kill all zombies on "
                     "one tile without taking damage. One time use."),
        item_type=ItemType.ESCAPE,
        combinable_with=[ItemName.CANDLE]
    ),

    ItemName.GASOLINE: ItemConfig(
        name=ItemName.GASOLINE,
        description=("Combine with Candle to kill all zombies without "
                     "taking damage. Combine with Chainsaw to give "
                     "two more chainsaw uses. One time use."),
        item_type=ItemType.COMBINE_ONLY,
        combinable_with=[ItemName.CANDLE, ItemName.CHAINSAW]
    ),

    ItemName.BOARD_WITH_NAILS: ItemConfig(
        name=ItemName.BOARD_WITH_NAILS,
        description="Add 1 to Attack score.",
        item_type=ItemType.WEAPON,
        attack_bonus=1,
        uses=99
    ),

    ItemName.CAN_OF_SODA: ItemConfig(
        name=ItemName.CAN_OF_SODA,
        description="Add 2 to Health points.",
        item_type=ItemType.HEALING,
        heal_amount=2
    ),

    ItemName.GRISLY_FEMUR: ItemConfig(
        name=ItemName.GRISLY_FEMUR,
        description="Add 1 to Attack score.",
        item_type=ItemType.WEAPON,
        attack_bonus=1,
        uses=99
    ),

    ItemName.GOLF_CLUB: ItemConfig(
        name=ItemName.GOLF_CLUB,
        description="Add 1 to Attack score.",
        item_type=ItemType.WEAPON,
        attack_bonus=1,
        uses=99
    ),

    ItemName.CANDLE: ItemConfig(
        name=ItemName.CANDLE,
        description=("Combine with Oil or Gasoline to kill all zombies "
                     "on one tile without taking damage."),
        item_type=ItemType.COMBINE_ONLY,
        combinable_with=[ItemName.OIL, ItemName.GASOLINE]
    ),

    ItemName.CHAINSAW: ItemConfig(
        name=ItemName.CHAINSAW,
        description=("Adds 3 to attack score. Only has enough fuel for "
                     "2 battles."),
        item_type=ItemType.WEAPON,
        attack_bonus=3,
        uses=2,
        combinable_with=[ItemName.GASOLINE]
    ),

    ItemName.MACHETE: ItemConfig(
        name=ItemName.MACHETE,
        description="Add 2 to Attack score.",
        item_type=ItemType.WEAPON,
        attack_bonus=2,
        uses=99
    )
}

# Number of uses gasoline adds to a chainsaw when combined
GASOLINE_CHAINSAW_USES = 2
