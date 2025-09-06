from src.enums_and_types import ItemName, ItemType
from .item import Item


class Weapon(Item):
    """Use this class for all weapons except chainsaw which has it's own class
    """

    def __init__(self, name: ItemName,
                 description: str,
                 attack_bonus: int) -> None:
        super().__init__(name, description, ItemType.WEAPON, attack_bonus)

    @property
    def uses_remaining(self) -> int:
        return 99

    def use(self) -> bool:
        return False
