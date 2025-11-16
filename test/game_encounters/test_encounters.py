import unittest

from src.enums_and_types import ItemName
from src.model import Player
from src.model.encounters.encounter import EncounterContext
from src.model.encounters.not_implemented_encounters import MessageEncounter, TotemEncounter
from src.model.encounters.item_encounter import ItemEncounter
from src.model.encounters.combat_encounter import CombatEncounter
from src.model.encounters.cower_encounter import CowerEncounter
from src.model.encounters.health_encounter import HealthEncounter
from src.model.item import get_item


class TestEncounters(unittest.TestCase):
    def setUp(self):
        self.player = Player(initial_health=4)
        self.encounter = EncounterContext(HealthEncounter(2))

    def test_health(self):
        self.encounter.use_encounter(self.player)
        self.assertEqual(self.player.get_health(), 6)

    def test_cower(self):
        cower = CowerEncounter()
        self.encounter.set_encounter(cower)
        self.encounter.use_encounter(self.player)
        self.assertEqual(self.player.get_health(), 7)

    def test_combat(self):
        combat = CombatEncounter(3)
        self.encounter.set_encounter(combat)
        self.encounter.use_encounter(self.player)
        self.assertEqual(self.player.get_health(), 2)

    def test_item(self):
        item = ItemEncounter(get_item(ItemName.GOLF_CLUB))
        self.encounter.set_encounter(item)
        self.encounter.use_encounter(self.player)
        self.assertEqual(self.player.get_inventory()[0].name, get_item(ItemName.GOLF_CLUB).name)

if __name__ == '__main__':
    unittest.main()
