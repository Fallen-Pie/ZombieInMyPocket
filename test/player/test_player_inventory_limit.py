import unittest
from unittest.mock import Mock
from src.model.player.player import Player
from src.model.interfaces.i_item import IItem


class TestPlayerInventoryLimit(unittest.TestCase):
    """User Story: Player Inventory Limit

    Given the player has a limited inventory space (2 items)
    When the player tries to pick up an item
    Then the system should enforce the inventory limit
    """

    def setUp(self):
        self.player = Player()

    def test_add_item_under_limit_success(self):
        """Acceptance Criteria (Success):
        Given the player's inventory has space
        When they pick up an item
        Then the item is added to their inventory
        """
        # Arrange
        mock_item = Mock(spec=IItem)

        # Act
        self.player.add_item_to_inventory(mock_item)

        # Assert
        self.assertIn(mock_item, self.player.get_inventory())

    def test_add_item_at_limit_failure(self):
        """Acceptance Criteria (Failure):
        Given the player's inventory is full (2 items)
        When they try to pick up another item
        Then the item is not added to their inventory
        """
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        mock_item3 = Mock(spec=IItem)

        # Fill inventory to capacity
        self.player.add_item_to_inventory(mock_item1)
        self.player.add_item_to_inventory(mock_item2)

        # Act - Try to add third item
        result = self.player.add_item_to_inventory(mock_item3)

        # Assert
        self.assertFalse(result)

        self.assertEqual(len(self.player.get_inventory()), 2)
        self.assertNotIn(mock_item3, self.player.get_inventory())
