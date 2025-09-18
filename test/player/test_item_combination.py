import unittest
from unittest.mock import patch
from src.model.player.player import Player
from src.model.item.base_item import ConsumableItem, SpecialWeaponItem
from src.enums_and_types.enums import ItemName, ItemType
from src.model.item.combination_engine import CombinationEngine
from src.model.item.combination_rules import CombinationResult

class TestItemCombination(unittest.TestCase):
    """Test class for player item combination."""

    def setUp(self):
        """Set up a new Player instance for each test."""
        self.player = Player()

    @patch.object(CombinationEngine, 'combine')
    def test_combine_items_success(self, mock_combine):
        """Test that two compatible items can be combined successfully, not implemented, will fail."""
        item1 = SpecialWeaponItem(name=ItemName.CHAINSAW, description="", attack_bonus=3, uses=1)
        item2 = ConsumableItem(name=ItemName.GASOLINE, description="", item_type=ItemType.ITEM, heal_amount=0)
        item1.combinable_with = [ItemName.GASOLINE]
        item2.combinable_with = [ItemName.CHAINSAW]

        mock_combine.return_value = CombinationResult(items_consumed=[item1, item2])

        self.player.add_item_to_inventory(item1)
        self.player.add_item_to_inventory(item2)

        result = self.player.combine_items_from_inventory()

        self.assertTrue(result)
        self.assertEqual(len(self.player.get_inventory()), 0)
        mock_combine.assert_called_once_with(item1, item2)

    @patch.object(CombinationEngine, 'combine')
    def test_combine_items_failure(self, mock_combine):
        """Test that incompatible items cannot be combined, not implemented, will fail."""
        item1 = SpecialWeaponItem(name=ItemName.CHAINSAW, description="", attack_bonus=3, uses=1)
        item2 = ConsumableItem(name=ItemName.CAN_OF_SODA, description="", item_type=ItemType.HEALING, heal_amount=2)

        mock_combine.side_effect = ValueError

        self.player.add_item_to_inventory(item1)
        self.player.add_item_to_inventory(item2)

        result = self.player.combine_items_from_inventory()

        self.assertFalse(result)
        self.assertEqual(len(self.player.get_inventory()), 2)
