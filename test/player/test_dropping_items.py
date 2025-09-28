import unittest
from unittest.mock import Mock
from src.model.player.player import Player
from src.model.interfaces.i_item import IItem


class TestDroppingItems(unittest.TestCase):
    """User Story: Dropping Items

    Given the player has an item in their inventory
    When the player drops the item
    Then the item should be removed from the player's inventory
    And the item should appear in the game world at the player's position
    """

    def setUp(self):
        self.player = Player()

    def test_drop_item_success(self):
        """Acceptance Criteria (Success):
        Given the player drops an item
        When the action is completed
        Then the player's inventory no longer contains the item and it is
        visible at their location

        Note: Only testing inventory removal. World placement would be
        handled by game logic.
        """
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player.add_item_to_inventory(mock_item)
        initial_inventory_length = len(self.player.get_inventory())

        # Act
        self.player.remove_item_from_inventory(mock_item)

        # Assert
        self.assertEqual(
            len(self.player.get_inventory()),
            initial_inventory_length - 1
        )
        self.assertNotIn(mock_item, self.player.get_inventory())

    def test_drop_item_from_empty_inventory_failure(self):
        """Acceptance Criteria (Failure):
        Given the player's inventory is empty
        When the player tries to drop an item
        Then no item is dropped and the game state does not change
        """
        # Arrange
        mock_item = Mock(spec=IItem)
        expected_inventory_length = 0

        # Act - Try to remove item not in inventory
        self.player.remove_item_from_inventory(mock_item)

        # Assert
        self.assertEqual(
            len(self.player.get_inventory()),
            expected_inventory_length
        )
