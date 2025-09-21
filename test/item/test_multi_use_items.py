import unittest
from src.model.item.base_item import SpecialWeaponItem
from src.enums_and_types import ItemName


class TestMultiUseItems(unittest.TestCase):
    """User Story: Multi-Use Items

    Given an unused chainsaw with 2 uses remaining
    When the chainsaw is used
    Then the uses remaining should be 1

    Given a chainsaw with 0 uses remaining
    When the chainsaw is used
    Then the uses remaining should stay at 0
    And the item cannot be used
    """

    def setUp(self):
        self.chainsaw = SpecialWeaponItem(
            name=ItemName.CHAINSAW,
            description="Motorized weapon",
            attack_bonus=3,
            uses=2
        )

    def test_multi_use_item_decreases_uses_success(self):
        """Acceptance Criteria (Success):
        Given an unused chainsaw with 2 uses remaining
        When the chainsaw is used
        Then the uses remaining should be 1
        """
        # Arrange
        self.assertEqual(self.chainsaw.uses_remaining, 2)

        # Act
        should_be_discarded = self.chainsaw.use()

        # Assert
        self.assertFalse(should_be_discarded)
        self.assertEqual(self.chainsaw.uses_remaining, 1)

    def test_multi_use_item_exhausted_failure(self):
        """Acceptance Criteria (Failure):
        Given a chainsaw with 0 uses remaining
        When the chainsaw is used
        Then the uses remaining should stay at 0
        And the item cannot be used
        """
        # Arrange
        self.chainsaw.use()  # 2 -> 1
        self.chainsaw.use()  # 1 -> 0
        self.assertEqual(self.chainsaw.uses_remaining, 0)

        # Act
        should_be_discarded = self.chainsaw.use()

        # Assert
        self.assertTrue(should_be_discarded)
        self.assertEqual(self.chainsaw.uses_remaining, 0)
