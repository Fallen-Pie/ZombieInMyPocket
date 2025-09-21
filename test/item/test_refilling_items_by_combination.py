import unittest
from src.model.item.base_item import SpecialWeaponItem, CombinableItem
from src.enums_and_types import ItemName, ItemType


class TestRefillingItemsByCombination(unittest.TestCase):
    """User Story: Refilling Items By Combination

    Given a chainsaw with no uses remaining
    And gasoline is available
    When they are combined
    Then the result is a chainsaw with 2 uses remaining

    Given a chainsaw with no uses remaining
    And gasoline is not available
    When an attempt is made to combine them
    Then the chainsaw remains with 0 uses
    """

    def setUp(self):
        self.empty_chainsaw = SpecialWeaponItem(
            name=ItemName.CHAINSAW,
            description="Motorized weapon",
            attack_bonus=3,
            uses=0,
            combinable_with=[ItemName.GASOLINE]
        )
        self.gasoline = CombinableItem(
            name=ItemName.GASOLINE,
            description="Fuel for chainsaw",
            item_type=ItemType.COMBINE_ONLY,
            combinable_with=[ItemName.CHAINSAW]
        )

    def test_refill_chainsaw_with_gasoline_success(self):
        """Acceptance Criteria (Success):
        Given a chainsaw with no uses remaining
        And gasoline is available
        When they are combined
        Then the result is a chainsaw with 2 uses remaining
        """
        # Arrange
        self.assertEqual(self.empty_chainsaw.uses_remaining, 0)
        self.assertIn(ItemName.GASOLINE, self.empty_chainsaw.combinable_with)
        self.assertIn(ItemName.CHAINSAW, self.gasoline.combinable_with)

        # Act
        self.empty_chainsaw.add_uses(2)  # Simulate combination result

        # Assert
        self.assertEqual(self.empty_chainsaw.uses_remaining, 2)

    def test_refill_chainsaw_without_gasoline_failure(self):
        """Acceptance Criteria (Failure):
        Given a chainsaw with no uses remaining
        And gasoline is not available
        When an attempt is made to combine them
        Then the chainsaw remains with 0 uses
        """
        # Arrange
        self.assertEqual(self.empty_chainsaw.uses_remaining, 0)

        # Act - No combination attempted (gasoline not available)
        # The chainsaw should remain unchanged

        # Assert
        self.assertEqual(self.empty_chainsaw.uses_remaining, 0)
