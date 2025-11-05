import unittest

from src.common import ItemName
from src.model import Player
from src.model.item import get_item
from src.model.encounters import *


class TestEncounters(unittest.TestCase):
    def setUp(self):
        self.player = Player(initial_health=4)

    def test_health(self):
        health = HealthEncounter(2)
        health.handle_encounter(self.player)
        self.assertEqual(self.player.get_health(), 6)

    def test_cower(self):
        cower = CowerEncounter()
        cower.handle_encounter(self.player)
        self.assertEqual(self.player.get_health(), 7)

    def test_combat(self):
        combat = CombatEncounter(3)
        combat.handle_encounter(self.player)
        self.assertEqual(self.player.get_health(), 2)

    def test_item(self):
        item = ItemEncounter(get_item(ItemName.GOLF_CLUB))
        item.handle_encounter(self.player)
        self.assertEqual(self.player.get_inventory()[0].name, get_item(ItemName.GOLF_CLUB).name)

    # def test_message(self):
    #     message = MessageEncounter(1)
    #     message.handle_encounter(self.player)
    #     self.assertEqual(1, 1)

    # def test_totem(self):
    #     totem = TotemEncounter(True)
    #     totem.handle_encounter(self.player)
    #     self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
