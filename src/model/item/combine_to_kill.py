from src.enums_and_types import ItemName, ItemType
from .item import Item


class CombineToKill(Item):
    """Base class for items that combine to kill all zombies.
    (Oil, Candle, and Gasoline)
    """

    def __init__(self, name: ItemName, description: str,
                 combinable_with: list[ItemName],
                 type: ItemType = ItemType.COMBINE_ONLY) -> None:
        super().__init__(name, description, type)
        self.__has_been_used = False
        self.__combinable_with = combinable_with

    @property
    def uses_remaining(self) -> int:
        """Number of uses remaining."""
        return 0 if self.__has_been_used else 1

    @property
    def combinable_with(self) -> list[ItemName]:
        return self.__combinable_with

    def use(self) -> bool:
        assert not self.__has_been_used
        self.__has_been_used = True
        return True
