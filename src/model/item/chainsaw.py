from src.enums_and_types.enums import ItemName
from .weapon import Weapon


class Chainsaw(Weapon):

    DESCRIPTION = ("Adds 3 to attack score. Only has enough fuel for "
                   "2 battles.")
    ATTACK_BONUS = 3
    START_FUEL = 2

    def __init__(self) -> None:
        super().__init__(ItemName.CHAINSAW,
                         Chainsaw.DESCRIPTION,
                         Chainsaw.ATTACK_BONUS)
        self._uses_remaining = Chainsaw.START_FUEL

    @property
    def uses_remaining(self) -> int:
        return self._uses_remaining

    @property
    def combinable_with(self) -> list[ItemName]:
        return [ItemName.GASOLINE]

    def use(self) -> bool:
        self._uses_remaining -= 1
        return self._uses_remaining <= 0

    def add_uses(self, amount: int):
        self._uses_remaining += amount
