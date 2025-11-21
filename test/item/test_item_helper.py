"""
Test suite for item_helper.py get_item() function.

This module tests all observable external behaviors of the get_item()
function (lines 22-65 in src/model/item/item_helper.py).

Tests cover all 9 branches of the match statement to achieve 100%
branch coverage for the target code block.

Can be run standalone:
    python -m unittest test.item.test_item_helper

Or with coverage:
    coverage run -m unittest test.item.test_item_helper
    coverage html --include="src/model/item/item_helper.py"
"""
from unittest import TestCase
from src.model.item.item_helper import get_item, IItem
from src.model.item.oil import Oil
from src.model.item.weapon import Weapon
from src.model.item.chainsaw import Chainsaw
from src.model.item.can_of_soda import CanOfSoda
from src.model.item.combine_to_kill import CombineToKill
from src.enums_and_types import ItemName, ItemType


class TestGetItemFunction(TestCase):
    """Test all branches of the get_item() function."""

    def test_get_item_oil_returns_oil_instance(self):
        """Test branch: ItemName.OIL returns Oil instance."""
        item = get_item(ItemName.OIL)
        self.assertIsInstance(item, Oil)
        self.assertEqual(item.name, ItemName.OIL)

    def test_get_item_oil_has_correct_properties(self):
        """Test Oil returned by get_item has expected properties."""
        item = get_item(ItemName.OIL)
        self.assertEqual(item.uses_remaining, 1)
        self.assertEqual(item.combinable_with, [ItemName.CANDLE])

    def test_get_item_gasoline_returns_combine_to_kill(self):
        """Test branch: ItemName.GASOLINE returns CombineToKill instance."""
        item = get_item(ItemName.GASOLINE)
        self.assertIsInstance(item, CombineToKill)
        self.assertEqual(item.name, ItemName.GASOLINE)

    def test_get_item_gasoline_has_correct_combinable_items(self):
        """Test Gasoline has correct combinable_with list."""
        item = get_item(ItemName.GASOLINE)
        self.assertIn(ItemName.CANDLE, item.combinable_with)
        self.assertIn(ItemName.CHAINSAW, item.combinable_with)

    def test_get_item_board_with_nails_returns_weapon(self):
        """Test branch: ItemName.BOARD_WITH_NAILS returns Weapon."""
        item = get_item(ItemName.BOARD_WITH_NAILS)
        self.assertIsInstance(item, Weapon)
        self.assertEqual(item.name, ItemName.BOARD_WITH_NAILS)

    def test_get_item_board_with_nails_has_attack_bonus_one(self):
        """Test Board with Nails weapon has attack bonus of 1."""
        item = get_item(ItemName.BOARD_WITH_NAILS)
        self.assertEqual(item.attack_bonus, 1)
        self.assertEqual(item.type, ItemType.WEAPON)

    def test_get_item_can_of_soda_returns_can_of_soda(self):
        """Test branch: ItemName.CAN_OF_SODA returns CanOfSoda instance."""
        item = get_item(ItemName.CAN_OF_SODA)
        self.assertIsInstance(item, CanOfSoda)
        self.assertEqual(item.name, ItemName.CAN_OF_SODA)

    def test_get_item_can_of_soda_is_health_item(self):
        """Test Can of Soda is categorized as health item."""
        item = get_item(ItemName.CAN_OF_SODA)
        self.assertEqual(item.type, ItemType.HEALING)

    def test_get_item_grisly_femur_returns_weapon(self):
        """Test branch: ItemName.GRISLY_FEMUR returns Weapon."""
        item = get_item(ItemName.GRISLY_FEMUR)
        self.assertIsInstance(item, Weapon)
        self.assertEqual(item.name, ItemName.GRISLY_FEMUR)

    def test_get_item_grisly_femur_has_attack_bonus_one(self):
        """Test Grisly Femur weapon has attack bonus of 1."""
        item = get_item(ItemName.GRISLY_FEMUR)
        self.assertEqual(item.attack_bonus, 1)

    def test_get_item_golf_club_returns_weapon(self):
        """Test branch: ItemName.GOLF_CLUB returns Weapon."""
        item = get_item(ItemName.GOLF_CLUB)
        self.assertIsInstance(item, Weapon)
        self.assertEqual(item.name, ItemName.GOLF_CLUB)

    def test_get_item_golf_club_has_attack_bonus_one(self):
        """Test Golf Club weapon has attack bonus of 1."""
        item = get_item(ItemName.GOLF_CLUB)
        self.assertEqual(item.attack_bonus, 1)

    def test_get_item_candle_returns_combine_to_kill(self):
        """Test branch: ItemName.CANDLE returns CombineToKill instance."""
        item = get_item(ItemName.CANDLE)
        self.assertIsInstance(item, CombineToKill)
        self.assertEqual(item.name, ItemName.CANDLE)

    def test_get_item_candle_has_correct_combinable_items(self):
        """Test Candle has correct combinable_with list."""
        item = get_item(ItemName.CANDLE)
        self.assertIn(ItemName.OIL, item.combinable_with)
        self.assertIn(ItemName.GASOLINE, item.combinable_with)

    def test_get_item_chainsaw_returns_chainsaw(self):
        """Test branch: ItemName.CHAINSAW returns Chainsaw instance."""
        item = get_item(ItemName.CHAINSAW)
        self.assertIsInstance(item, Chainsaw)
        self.assertEqual(item.name, ItemName.CHAINSAW)

    def test_get_item_chainsaw_has_two_uses(self):
        """Test Chainsaw starts with 2 uses."""
        item = get_item(ItemName.CHAINSAW)
        self.assertEqual(item.uses_remaining, 2)

    def test_get_item_chainsaw_has_attack_bonus_three(self):
        """Test Chainsaw has attack bonus of 3."""
        item = get_item(ItemName.CHAINSAW)
        self.assertEqual(item.attack_bonus, 3)

    def test_get_item_machete_returns_weapon(self):
        """Test branch: ItemName.MACHETE returns Weapon."""
        item = get_item(ItemName.MACHETE)
        self.assertIsInstance(item, Weapon)
        self.assertEqual(item.name, ItemName.MACHETE)

    def test_get_item_machete_has_attack_bonus_two(self):
        """Test Machete weapon has attack bonus of 2."""
        item = get_item(ItemName.MACHETE)
        self.assertEqual(item.attack_bonus, 2)

    def test_all_items_implement_iitem_interface(self):
        """Test all items returned implement IItem interface."""
        for item_name in [ItemName.OIL, ItemName.GASOLINE,
                          ItemName.BOARD_WITH_NAILS, ItemName.CAN_OF_SODA,
                          ItemName.GRISLY_FEMUR, ItemName.GOLF_CLUB,
                          ItemName.CANDLE, ItemName.CHAINSAW,
                          ItemName.MACHETE]:
            with self.subTest(item=item_name):
                item = get_item(item_name)
                # Verify IItem interface methods exist
                self.assertTrue(hasattr(item, 'name'))
                self.assertTrue(hasattr(item, 'use'))
                self.assertTrue(hasattr(item, 'uses_remaining'))
                self.assertTrue(hasattr(item, 'combinable_with'))
                self.assertTrue(hasattr(item, 'type'))
                self.assertTrue(hasattr(item, 'description'))

    def test_all_items_return_iitem_type(self):
        """Test all get_item calls return IItem interface type."""
        for item_name in [ItemName.OIL, ItemName.GASOLINE,
                          ItemName.BOARD_WITH_NAILS, ItemName.CAN_OF_SODA,
                          ItemName.GRISLY_FEMUR, ItemName.GOLF_CLUB,
                          ItemName.CANDLE, ItemName.CHAINSAW,
                          ItemName.MACHETE]:
            with self.subTest(item=item_name):
                item = get_item(item_name)
                self.assertIsInstance(item, IItem)

    def test_get_item_returns_new_instance_each_call(self):
        """Test get_item returns new instance on each call."""
        item1 = get_item(ItemName.OIL)
        item2 = get_item(ItemName.OIL)
        # Should be different instances
        self.assertIsNot(item1, item2)
        # But same type and properties
        self.assertEqual(type(item1), type(item2))
        self.assertEqual(item1.name, item2.name)

    def test_weapons_have_correct_attack_bonuses(self):
        """Test all weapons have appropriate attack bonuses."""
        # Attack bonus 1 weapons
        for weapon_name in [ItemName.BOARD_WITH_NAILS,
                            ItemName.GRISLY_FEMUR,
                            ItemName.GOLF_CLUB]:
            with self.subTest(weapon=weapon_name):
                weapon = get_item(weapon_name)
                self.assertEqual(weapon.attack_bonus, 1)

        # Attack bonus 2 weapon
        machete = get_item(ItemName.MACHETE)
        self.assertEqual(machete.attack_bonus, 2)

        # Attack bonus 3 weapon
        chainsaw = get_item(ItemName.CHAINSAW)
        self.assertEqual(chainsaw.attack_bonus, 3)

    def test_combine_to_kill_items_have_combinable_lists(self):
        """Test CombineToKill items have non-empty combinable_with lists."""
        gasoline = get_item(ItemName.GASOLINE)
        self.assertGreater(len(gasoline.combinable_with), 0)

        candle = get_item(ItemName.CANDLE)
        self.assertGreater(len(candle.combinable_with), 0)

    def test_get_item_descriptions_are_strings(self):
        """Test all items have string descriptions."""
        for item_name in [ItemName.OIL, ItemName.GASOLINE,
                          ItemName.BOARD_WITH_NAILS, ItemName.CAN_OF_SODA,
                          ItemName.GRISLY_FEMUR, ItemName.GOLF_CLUB,
                          ItemName.CANDLE, ItemName.CHAINSAW,
                          ItemName.MACHETE]:
            with self.subTest(item=item_name):
                item = get_item(item_name)
                self.assertIsInstance(item.description, str)
                self.assertGreater(len(item.description), 0)


if __name__ == '__main__':
    # Run with: python -m unittest test.item.test_item_helper
    # Or: python test_item_helper.py (if in test/item/ directory)
    import unittest
    unittest.main(verbosity=2)
