from enum import Enum

class ItemType(Enum):
    WEAPON = 0
    HEALING = 1  # Can of Soda
    COMBINE_ONLY = 2  # Candle and Gasoline
    ESCAPE = 3  # Using oil by itself without combining it

class ItemName(Enum):
    OIL = "Oil"
    GASOLINE = "Gasoline"
    BOARD_WITH_NAILS = "Board With Nails"
    CAN_OF_SODA = "Can of Soda"
    GRISLY_FEMUR = "Grisly Femur"
    GOLF_CLUB = "Golf Club"
    CANDLE = "Candle"
    CHAINSAW = "Chainsaw"
    MACHETE = "Machete"

class ItemInfo(Enum):
    # SPADE = ("Spade", "A sturdy digging tool that can be used as a weapon", ItemType.WEAPON, 2, 0, False,
    #          cast(list['ItemInfo'], []))
    # AXE = ("Axe", "A sharp wood-cutting axe effective in combat", ItemType.WEAPON, 3, 0, False,
    #        cast(list['ItemInfo'], []))
    # BANDAGE = ("Bandage", "Basic medical supplies for treating wounds", ItemType.HEALING, 0, 3, True,
    #            cast(list['ItemInfo'], []))
    # HEALTH_KIT = ("Health Kit", "Advanced medical kit for serious injuries", ItemType.HEALING, 0, 8, True,
    #               cast(list['ItemInfo'], []))

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
