from src.enums_and_types import ItemName, ItemType
from ..interfaces import IItem


class Item(IItem):
    def __init__(self, name: ItemName,
                 description: str,
                 type: ItemType,
                 attack_bonus: int = 0,
                 heal_amount: int = 0) -> None:
        self.__name = name
        self.__description = description
        self.__type = type
        self.__attack_bonus = attack_bonus
        self.__heal_amount = heal_amount

    @property
    def name(self) -> ItemName:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def type(self) -> ItemType:
        return self.__type

    @property
    def attack_bonus(self) -> int:
        return self.__attack_bonus

    @property
    def heal_amount(self) -> int:
        return self.__heal_amount

    @property
    def combinable_with(self) -> list[ItemName]:
        return []
