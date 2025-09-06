from ..interfaces.i_dev_card import IDevCard
from ..interfaces.i_item import IItem
from ..item import get_item
from src.enums_and_types import ItemName
from ..encounters.encounters import *


class DevCard(IDevCard):

    def __init__(self, item: IItem,
                 encounter_9pm: IEncounter,
                 encounter_10pm: IEncounter,
                 encounter_11pm: IEncounter) -> None:
        self._item = item
        self._encounters = (encounter_9pm, encounter_10pm, encounter_11pm)

    def get_item(self) -> IItem:
        return self._item

    def get_encounter(self, time: int) -> IEncounter:
        assert 9 <= time <= 11, \
            f"Cannot get an ecounter from dev card at time {time}pm"
        return self._encounters[time - 9]

    @staticmethod
    def get_dev_cards() -> list[IDevCard]:
        return [
            DevCard(
                get_item(ItemName.OIL),
                MessageEncounter("You try hard not to wet yourself."),
                ItemEncounter(None),
                CombatEncounter(6)
            ),
            DevCard(
                get_item(ItemName.GASOLINE),
                CombatEncounter(4),
                HealthEncounter(-1),
                ItemEncounter(None)
            ),
            DevCard(
                get_item(ItemName.BOARD_WITH_NAILS),
                ItemEncounter(None),
                CombatEncounter(4),
                HealthEncounter(-1)
            ),
            DevCard(
                get_item(ItemName.MACHETE),
                CombatEncounter(4),
                HealthEncounter(-1),
                CombatEncounter(6)
            ),
            DevCard(
                get_item(ItemName.GRISLY_FEMUR),
                ItemEncounter(None),
                CombatEncounter(5),
                HealthEncounter(1)
            ),
            DevCard(
                get_item(ItemName.GOLF_CLUB),
                HealthEncounter(-1),
                CombatEncounter(4),
                MessageEncounter("The smell of blood is in the air.")
            ),
            DevCard(
                get_item(ItemName.CHAINSAW),
                CombatEncounter(3),
                MessageEncounter("You hear terrible screams."),
                CombatEncounter(5)
            ),
            DevCard(
                get_item(ItemName.CAN_OF_SODA),
                HealthEncounter(1),
                ItemEncounter(None),
                CombatEncounter(4)
            ),
            DevCard(
                get_item(ItemName.CANDLE),
                MessageEncounter("Your body shivers involuntarily"),
                HealthEncounter(1),
                CombatEncounter(4)
            ),
        ]
