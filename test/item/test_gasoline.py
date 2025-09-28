from unittest import TestCase
from src.model.item.item_helper import IItem, get_item
from src.enums_and_types import ItemName, ItemType


class TestGasoline(TestCase):

    def setUp(self):
        self._item: IItem = get_item(ItemName.GASOLINE)

    def test_name_is_gasoline(self):
        expected = ItemName.GASOLINE
        actual = self._item.name
        self.assertEqual(expected, actual)

    def test_type_is_combine_only(self):
        expected = ItemType.COMBINE_ONLY
        actual = self._item.type
        self.assertEqual(expected, actual)

    def test_uses_is_one(self):
        expected = 1
        actual = self._item.uses_remaining
        self.assertEqual(expected, actual)

    def test_using_item_uses_up_use(self):
        self._item.use()
        expected = 0
        actual = self._item.uses_remaining
        self.assertEqual(expected, actual)

    def test_combinable_with_candle(self):
        self.assertIn(ItemName.CANDLE, self._item.combinable_with)

    def test_combinable_with_chainsaw(self):
        self.assertIn(ItemName.CHAINSAW, self._item.combinable_with)
