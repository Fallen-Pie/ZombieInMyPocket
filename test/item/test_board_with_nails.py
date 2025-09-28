from unittest import TestCase
from src.model.item.item_helper import IItem, get_item
from src.enums_and_types import ItemName, ItemType


class TestBoardWithNails(TestCase):

    def setUp(self):
        self._item: IItem = get_item(ItemName.BOARD_WITH_NAILS)

    def test_name_is_board_with_nails(self):
        expected = ItemName.BOARD_WITH_NAILS
        actual = self._item.name
        self.assertEqual(expected, actual)

    def test_type_is_weapon(self):
        expected = ItemType.WEAPON
        actual = self._item.type
        self.assertEqual(expected, actual)

    def test_uses_is_at_least_one(self):
        self.assertGreaterEqual(self._item.uses_remaining, 1)

    def test_using_item_does_not_use_up_use(self):
        self._item.use()
        self.assertGreaterEqual(self._item.uses_remaining, 1)

    def test_combinable_with_nothing(self):
        expected = []
        actual = self._item.combinable_with
        self.assertEqual(expected, actual)

    def test_attack_bonus_is_one(self):
        expected = 1
        actual = self._item.attack_bonus
        self.assertEqual(expected, actual)
