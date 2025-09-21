"""
Item module for the Zombie in My Pocket game.

This module provides item creation, management, and combination functionality.
It exposes the main interfaces for working with game items including:
- Creating individual items
- Getting all available items  
- Combining items according to game rules
"""

from .item_factory import get_item, get_all_items
from .combination_engine import combine_items


__all__ = [
    'get_item',
    'get_all_items',
    'combine_items',
]
