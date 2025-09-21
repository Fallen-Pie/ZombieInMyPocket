import unittest
from unittest.mock import Mock
from src.model.player.player import Player

class TestInventoryManagement(unittest.TestCase):
    """Test class for player inventory management."""

    def setUp(self):
        """Set up a new Player instance for each test."""
        self.player = Player()

    def test_add_item_to_inventory(self):
        """Test that items can be added to the inventory."""
        item1 = Mock()
        self.player.add_item_to_inventory(item1)
        self.assertIn(item1, self.player.get_inventory())

    def test_inventory_limit(self):
        """Test that the inventory has a limit."""
        item1 = Mock()
        item2 = Mock()
        item3 = Mock()
        self.player.add_item_to_inventory(item1)
        self.player.add_item_to_inventory(item2)
        self.player.add_item_to_inventory(item3)
        self.assertEqual(len(self.player.get_inventory()), 2)
        self.assertNotIn(item3, self.player.get_inventory())

    def test_remove_item_from_inventory(self):
        """Test that items can be removed from the inventory."""
        item1 = Mock()
        self.player.add_item_to_inventory(item1)
        self.assertIn(item1, self.player.get_inventory())
        self.player.remove_item_from_inventory(item1)
        self.assertNotIn(item1, self.player.get_inventory())
