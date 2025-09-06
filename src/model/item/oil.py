from src.enums_and_types import ItemName, ItemType
from .combine_to_kill import CombineToKill


class Oil(CombineToKill):

    DESCRIPTION = ("Throw as you run away to avoid taking damage. "
                   "Combine with Candle to kill all zombies on "
                   "one tile without taking damage. One time use.")

    def __init__(self) -> None:
        super().__init__(ItemName.OIL, Oil.DESCRIPTION,
                         [ItemName.CANDLE],
                         ItemType.ESCAPE)
