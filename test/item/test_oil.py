from unittest import TestCase
from src.model.item.item_helper import IItem, get_item
from src.enums_and_types import ItemName


class TestOil(TestCase):

    def setUp(self):
        self._item: IItem = get_item(ItemName.OIL)

    def test_name_is_oil(self):
        expected = ItemName.OIL
        actual = self._item.name
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
        expected = [ItemName.CANDLE]
        actual = self._item.combinable_with
        self.assertEqual(expected, actual)
