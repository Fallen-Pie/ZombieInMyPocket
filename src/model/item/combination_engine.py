"""Engine for managing item combination logic in Zombie in My Pocket.

This module handles the combination of items according to predefined rules,
allowing items to be combined for special effects like killing all zombies
or enhancing weapon capabilities.
"""

from ..interfaces import IItem
from .combination_rules import (
    CombinationRule,
    CombinationResult,
    CandleWithFlammableRule,
    ChainsawWithGasolineRule
)


class CombinationEngine:
    """Manages item combination rules and processes combination requests.
    
    The engine maintains a list of combination rules and applies them to
    determine if and how items can be combined together.
    """
    def __init__(self):
        """Initialize the combination engine with default rules."""
        self._rules: list[CombinationRule] = [
            CandleWithFlammableRule(),
            ChainsawWithGasolineRule()
        ]

    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        """Check if two items can be combined.
        
        Args:
            item_a: First item to combine
            item_b: Second item to combine
            
        Returns:
            True if the items can be combined, False otherwise
        """
        if not self._basic_combination_check(item_a, item_b):
            return False

        return any(rule.can_combine(item_a, item_b) for rule in self._rules)

    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        """Combine two items according to applicable rules.
        
        Args:
            item_a: First item to combine
            item_b: Second item to combine
            
        Returns:
            Result of the combination including effects and consumed items
            
        Raises:
            ValueError: If the items cannot be combined
        """
        if not self._basic_combination_check(item_a, item_b):
            raise ValueError("Items cannot be combined")

        for rule in self._rules:
            if rule.can_combine(item_a, item_b):
                return rule.combine(item_a, item_b)

        raise ValueError("No combination rule found for these items")

    def _basic_combination_check(self, item_a: IItem, item_b: IItem) -> bool:
        """Check if items are mutually combinable.
        
        Args:
            item_a: First item to check
            item_b: Second item to check
            
        Returns:
            True if both items list each other as combinable
        """
        return (item_a.name in item_b.combinable_with and
                item_b.name in item_a.combinable_with)


_combination_engine = CombinationEngine()


def combine_items(item_a: IItem, item_b: IItem) -> bool:
    """Convenience function to combine two items.
    
    Args:
        item_a: First item to combine
        item_b: Second item to combine
        
    Returns:
        True if the combination kills all zombies, False otherwise
        
    Raises:
        ValueError: If the items cannot be combined
    """
    if not _combination_engine.can_combine(item_a, item_b):
        raise ValueError("Items cannot be combined")

    result = _combination_engine.combine(item_a, item_b)
    return result.kills_all_zombies
