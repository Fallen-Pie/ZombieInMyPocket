from src.enums_and_types import ItemName, ItemType
from .item import Item


class CanOfSoda(Item):

    DESCRIPTION = "Add 2 to Health points."

    def __init__(self) -> None:
        super().__init__(
            ItemName.CAN_OF_SODA,
            CanOfSoda.DESCRIPTION,
            ItemType.HEALING,
            heal_amount=2
        )
        self.__has_been_used = False

    @property
    def uses_remaining(self) -> int:
        """Number of uses remaining."""
        return 0 if self.__has_been_used else 1

    def use(self) -> bool:
        assert not self.__has_been_used
        self.__has_been_used = True
        return True
