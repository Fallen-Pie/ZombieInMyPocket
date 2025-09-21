import unittest
from src.model.player.player import Player
from src.model.item.base_item import ConsumableItem, WeaponItem
from src.enums_and_types.enums import ItemName, ItemType

class TestItemUsage(unittest.TestCase):
    """Test class for player item usage."""

    def setUp(self):
        """Set up a new Player instance for each test."""
        self.player = Player()

    def test_use_consumable_item(self):
        """Test using a consumable item like a can of soda."""
        self.player.take_damage(3)
        self.assertEqual(self.player.get_health(), 3)
        soda = ConsumableItem(name=ItemName.CAN_OF_SODA, description="", item_type=ItemType.HEALING, heal_amount=2)
        self.player.add_item_to_inventory(soda)
        self.player.use_item(soda)
        self.assertEqual(self.player.get_health(), 5)
        self.assertEqual(len(self.player.get_inventory()), 0)

    def test_use_weapon_item(self):
        """Test using a weapon item."""
        machete = WeaponItem(name=ItemName.MACHETE, description="", attack_bonus=2, uses=1)
        self.player.add_item_to_inventory(machete)
        self.assertEqual(self.player.get_attack_power(), 3)
        self.player.use_item(machete)
        self.assertEqual(len(self.player.get_inventory()), 0)
        self.assertEqual(self.player.get_attack_power(), 1)

    def test_use_multi_use_weapon_item(self):
        """Test using a multi-use weapon item."""
        chainsaw = WeaponItem(name=ItemName.CHAINSAW, description="", attack_bonus=3, uses=2)
        self.player.add_item_to_inventory(chainsaw)
        self.assertEqual(self.player.get_attack_power(), 4)
        self.player.use_item(chainsaw)
        self.assertEqual(len(self.player.get_inventory()), 1)
        self.assertEqual(self.player.get_attack_power(), 4)
        self.player.use_item(chainsaw)
        self.assertEqual(len(self.player.get_inventory()), 0)
        self.assertEqual(self.player.get_attack_power(), 1)
