"""Rules and result types for item combinations in Zombie in My Pocket.

This module defines the abstract base for combination rules and specific
implementations for different item combination effects like candle + oil
and chainsaw + gasoline combinations.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from src.enums_and_types import ItemName
from ..interfaces import IItem
from .base_item import SpecialWeaponItem
from .item_config import GASOLINE_CHAINSAW_USES


@dataclass
class CombinationResult:
    """Result of combining two items.
    
    Attributes:
        kills_all_zombies: Whether this combination kills all zombies on the tile
        items_consumed: List of items that are consumed in the combination
    """
    kills_all_zombies: bool = False
    items_consumed: list[IItem] = None

    def __post_init__(self):
        """Initialize items_consumed to empty list if None."""
        if self.items_consumed is None:
            self.items_consumed = []


class CombinationRule(ABC):
    """Abstract base class for item combination rules.
    
    Each combination rule defines which items can be combined together
    and what effects occur when they are combined.
    """
    @abstractmethod
    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        """Check if two items can be combined under this rule.
        
        Args:
            item_a: First item to check
            item_b: Second item to check
            
        Returns:
            True if the items can be combined under this rule
        """
        pass

    @abstractmethod
    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        """Combine two items according to this rule.
        
        Args:
            item_a: First item to combine
            item_b: Second item to combine
            
        Returns:
            Result of the combination including effects and consumed items
        """
        pass


class CandleWithFlammableRule(CombinationRule):
    """Rule for combining candles with flammable items (oil or gasoline).
    
    This combination creates a fire effect that kills all zombies on the
    current tile without the player taking damage.
    """
    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        """Check if items are candle + flammable combination.
        
        Args:
            item_a: First item to check
            item_b: Second item to check
            
        Returns:
            True if one item is a candle and the other is oil or gasoline
        """
        return ((item_a.name == ItemName.CANDLE and
                 item_b.name in [ItemName.OIL, ItemName.GASOLINE]) or
                (item_b.name == ItemName.CANDLE and
                 item_a.name in [ItemName.OIL, ItemName.GASOLINE]))

    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        """Combine candle with flammable item to kill all zombies.
        
        Args:
            item_a: First item (candle or flammable)
            item_b: Second item (flammable or candle)
            
        Returns:
            Result indicating all zombies are killed and items consumed
        """
        item_a.use()
        item_b.use()

        consumed = []
        if item_a.uses_remaining <= 0:
            consumed.append(item_a)
        if item_b.uses_remaining <= 0:
            consumed.append(item_b)

        return CombinationResult(
            kills_all_zombies=True,
            items_consumed=consumed
        )


class ChainsawWithGasolineRule(CombinationRule):
    """Rule for combining chainsaw with gasoline to refuel it.
    
    This combination adds additional uses to the chainsaw weapon,
    consuming the gasoline in the process.
    """

    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        """Check if items are chainsaw + gasoline combination.
        
        Args:
            item_a: First item to check
            item_b: Second item to check
            
        Returns:
            True if one item is a chainsaw and the other is gasoline
        """
        return ((item_a.name == ItemName.CHAINSAW and
                 item_b.name == ItemName.GASOLINE) or
                (item_b.name == ItemName.CHAINSAW and
                 item_a.name == ItemName.GASOLINE))

    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        """Combine chainsaw with gasoline to refuel the chainsaw.
        
        Args:
            item_a: First item (chainsaw or gasoline)
            item_b: Second item (gasoline or chainsaw)
            
        Returns:
            Result indicating gasoline is consumed and chainsaw is refueled
        """
        chainsaw = None
        gasoline = None

        if item_a.name == ItemName.CHAINSAW:
            chainsaw = item_a
            gasoline = item_b
        else:
            chainsaw = item_b
            gasoline = item_a

        if isinstance(chainsaw, SpecialWeaponItem):
            chainsaw.add_uses(GASOLINE_CHAINSAW_USES)

        gasoline.use()

        consumed = []
        if gasoline.uses_remaining <= 0:
            consumed.append(gasoline)

        return CombinationResult(
            kills_all_zombies=False,
            items_consumed=consumed
        )
