from enum import Enum
from typing import cast

from .item_type import ItemType


class ItemInfo(Enum):
    SPADE = ("Spade", "A sturdy digging tool that can be used as a weapon", ItemType.WEAPON, 2, 0, False,
             cast(list['ItemInfo'], []))
    AXE = (
    "Axe", "A sharp wood-cutting axe effective in combat", ItemType.WEAPON, 3, 0, False, cast(list['ItemInfo'], []))
    BANDAGE = (
    "Bandage", "Basic medical supplies for treating wounds", ItemType.HEALING, 0, 3, True, cast(list['ItemInfo'], []))
    HEALTH_KIT = (
    "Health Kit", "Advanced medical kit for serious injuries", ItemType.HEALING, 0, 8, True, cast(list['ItemInfo'], []))

    def __init__(self, display_name: str, description: str, item_type: ItemType,
                 attack_bonus: int, heal_amount: int, is_single_use: bool,
                 combinable_with: list['ItemInfo']):
        self.display_name = display_name
        self.description = description
        self.item_type = item_type
        self.attack_bonus = attack_bonus
        self.heal_amount = heal_amount
        self.is_single_use = is_single_use
        self.combinable_with = combinable_with