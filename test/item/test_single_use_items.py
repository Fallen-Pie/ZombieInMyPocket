import unittest
from src.model.item.base_item import ConsumableItem
from src.enums_and_types import ItemName, ItemType


class TestSingleUseItems(unittest.TestCase):
    """User Story: Single Use Items

    Given an item is single use
    When the item is used
    Then the uses remaining should be 0

    Given an item is single use and already has 0 uses remaining
    When the item is used
    Then the uses remaining should stay at 0
    And the item cannot be used again
    """

    def setUp(self):
        self.single_use_item = ConsumableItem(
            name=ItemName.CAN_OF_SODA,
            description="Healing item",
            item_type=ItemType.HEALING,
            heal_amount=3
        )

    def test_single_use_item_becomes_exhausted_success(self):
        """Acceptance Criteria (Success):
        Given an item is single use
        When the item is used
        Then the uses remaining should be 0
        """
        # Arrange
        self.assertEqual(self.single_use_item.uses_remaining, 1)

        # Act
        should_be_discarded = self.single_use_item.use()

        # Assert
        self.assertTrue(should_be_discarded)
        self.assertEqual(self.single_use_item.uses_remaining, 0)

    def test_single_use_item_already_exhausted_failure(self):
        """Acceptance Criteria (Failure):
        Given an item is single use and already has 0 uses remaining
        When the item is used
        Then the uses remaining should stay at 0
        And the item cannot be used again
        """
        # Arrange
        self.single_use_item.use()  # Exhaust the item
        self.assertEqual(self.single_use_item.uses_remaining, 0)

        # Act
        should_be_discarded = self.single_use_item.use()

        # Assert
        self.assertTrue(should_be_discarded)
        self.assertEqual(self.single_use_item.uses_remaining, 0)
