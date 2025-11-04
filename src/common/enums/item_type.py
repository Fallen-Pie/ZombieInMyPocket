from enum import Enum


class ItemType(Enum):
    WEAPON = 0
    HEALING = 1  # Can of Soda
    COMBINE_ONLY = 2  # Candle and Gasoline
    ESCAPE = 3  # Using oil by itself without combining it