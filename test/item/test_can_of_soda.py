from unittest import TestCase
from src.model.item.item_helper import IItem, get_item
from src.enums_and_types import ItemName, ItemType


class TestCanOfSoda(TestCase):

    def setUp(self):
        self._item: IItem = get_item(ItemName.CAN_OF_SODA)

    def test_name_is_can_of_soda(self):
        expected = ItemName.CAN_OF_SODA
        actual = self._item.name
        self.assertEqual(expected, actual)

    def test_type_is_healing(self):
        expected = ItemType.HEALING
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

    def test_combinable_with_nothing(self):
        expected = []
        actual = self._item.combinable_with
        self.assertEqual(expected, actual)

    def test_health_bonus_is_two(self):
        expected = 2
        actual = self._item.heal_amount
        self.assertEqual(expected, actual)
