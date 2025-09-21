import unittest
from src.model.player.player import Player
from src.model.item.base_item import WeaponItem
from src.enums_and_types.enums import ItemName

class TestPlayerState(unittest.TestCase):
    """Test class for player state management."""

    def setUp(self):
        """Set up a new Player instance for each test."""
        self.player = Player()

    def test_initial_state(self):
        """Test that the player is initialized with the correct default values."""
        self.assertEqual(self.player.get_health(), 6)
        self.assertEqual(self.player.get_attack_power(), 1)
        self.assertFalse(self.player.has_totem())
        self.assertEqual(self.player.get_position(), (0, 0))

    def test_take_damage(self):
        """Test that the player's health is correctly reduced when taking damage."""
        self.player.take_damage(2)
        self.assertEqual(self.player.get_health(), 4)
        self.player.take_damage(10)
        self.assertEqual(self.player.get_health(), 0)
        self.player.take_damage(-5)  # Should not do anything
        self.assertEqual(self.player.get_health(), 0)

    def test_heal(self):
        """Test that the player's health is correctly increased when healing."""
        self.player.take_damage(4)
        self.assertEqual(self.player.get_health(), 2)
        self.player.heal(3)
        self.assertEqual(self.player.get_health(), 5)
        self.player.heal(10)
        self.assertEqual(self.player.get_health(), 6)
        self.player.heal(-5)  # Should not do anything
        self.assertEqual(self.player.get_health(), 6)

    def test_attack_power_with_weapon(self):
        """Test that the player's attack power is increased by weapons."""
        self.assertEqual(self.player.get_attack_power(), 1)
        machete = WeaponItem(name=ItemName.MACHETE, description="", attack_bonus=2)
        self.player.add_item_to_inventory(machete)
        self.assertEqual(self.player.get_attack_power(), 3)
        self.player.remove_item_from_inventory(machete)
        self.assertEqual(self.player.get_attack_power(), 1)

    def test_set_position(self):
        """Test that the player's position can be updated."""
        self.player.set_position((3, 4))
        self.assertEqual(self.player.get_position(), (3, 4))

    def test_set_has_totem(self):
        """Test that the player's totem status can be updated."""
        self.assertFalse(self.player.has_totem())
        self.player.set_has_totem(True)
        self.assertTrue(self.player.has_totem())
