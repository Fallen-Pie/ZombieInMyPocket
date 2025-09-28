import unittest
from unittest.mock import Mock
from src.model.player.player import Player
from src.model.interfaces.i_item import IItem


class TestUsingItems(unittest.TestCase):
    """User Story: Using Items

    Given the player has an item in their inventory
    When the player uses the item
    Then the item's effect should be applied to the player
    """

    def setUp(self):
        self.player = Player()

    def test_use_health_potion_success(self):
        """Acceptance Criteria (Success):
        Given the player has a health potion
        When they use the potion
        Then the player's health increases by the potion's value
        """
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1  # HEALING
        mock_item.heal_amount = 25
        mock_item.uses_remaining = 1
        self.player.add_item_to_inventory(mock_item)
        initial_health = self.player.get_health()

        # Act
        self.player.use_item(mock_item)

        # Assert
        self.assertEqual(self.player.get_health(), initial_health + 25)

    def test_use_item_no_usable_items_failure(self):
        """Acceptance Criteria (Failure):
        Given the player has no usable items
        When they attempt to use an item
        Then nothing happens
        """
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1
        mock_item.heal_amount = 25
        expected_health = 100

        # Act - Try to use item not in inventory
        self.player.use_item(mock_item)

        # Assert
        self.assertEqual(self.player.get_health(), expected_health)
