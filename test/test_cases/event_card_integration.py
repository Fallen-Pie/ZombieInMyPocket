import unittest

from src.model import DevCard

class EventCardIntegration(unittest.TestCase):
    """
    Event Card Integration
    • Given the player enters a tile,
    • When an event card spawning zombies is drawn and triggered,
    • Then the correct number of zombies appears on the tile.
    """
    def setUp(self):
        self.dev_card_list = DevCard.get_dev_cards()
        self.dev_card_one = self.dev_card_list.pop(0)
        self.dev_card_two = self.dev_card_list.pop(0)

    def test_combat_one(self):
        encounter = self.dev_card_one.get_encounter(11)
        self.assertEqual(encounter.zombies, 6)

    def test_combat_two(self):
        encounter = self.dev_card_two.get_encounter(9)
        self.assertEqual(encounter.zombies, 4)

if __name__ == '__main__':
    unittest.main()
