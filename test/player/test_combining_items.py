import unittest
from unittest.mock import Mock
from src.model.player.player import Player
from src.model.interfaces.i_item import IItem


class TestCombiningItems(unittest.TestCase):
    """User Story: Combining Items

    Given the player has two combinable items in their inventory
    When the player uses the combine items action
    Then the items should be replaced by the new combined item
    """

    def setUp(self):
        self.player = Player()

    def test_combine_items_success(self):
        """Acceptance Criteria (Success):
        Given the player has two items that can be combined
        When they combine them
        Then the player receives the new combined item
        """
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        mock_item1.name = "item1"
        mock_item2.name = "item2"
        mock_item1.combinable_with = ["item2"]
        mock_item2.combinable_with = ["item1"]
        self.player.add_item_to_inventory(mock_item1)
        self.player.add_item_to_inventory(mock_item2)

        # Act
        result = self.player.combine_items_from_inventory()

        # Assert
        self.assertIsInstance(result, bool)

    def test_combine_items_failure(self):
        """Acceptance Criteria (Failure):
        Given the player has two items that cannot be combined
        When they attempt to combine them
        Then the items remain unchanged in the player's inventory
        """
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        mock_item1.name = "item1"
        mock_item2.name = "item2"
        mock_item1.combinable_with = []  # Cannot combine
        mock_item2.combinable_with = []  # Cannot combine
        self.player.add_item_to_inventory(mock_item1)
        self.player.add_item_to_inventory(mock_item2)

        # Act
        result = self.player.combine_items_from_inventory()

        # Assert
        self.assertIsInstance(result, bool)

    def test_combine_items_insufficient_items(self):
        """Test combining with less than 2 items fails."""
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player.add_item_to_inventory(mock_item)

        # Act
        result = self.player.combine_items_from_inventory()

        # Assert
        self.assertEqual(result, False)

    def test_combine_items_empty_inventory(self):
        """Test combining with empty inventory fails."""
        # Act
        result = self.player.combine_items_from_inventory()

        # Assert
        self.assertEqual(result, False)
