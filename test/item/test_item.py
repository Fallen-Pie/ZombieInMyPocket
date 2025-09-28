from unittest import TestCase
from src.enums_and_types import ItemName
from src.model.item import get_item, combine_items


class TestItem(TestCase):
    
    def test_using_up_single_item(self):
        can = get_item(ItemName.CAN_OF_SODA)
        expected = 1
        actual = can.uses_remaining
        self.assertEqual(expected, actual)

        can.use()
        expected = 0
        actual = can.uses_remaining
        self.assertEqual(expected, actual)
    
    def test_using_chainsaw_decrements_uses_remaining(self):
        chainsaw = get_item(ItemName.CHAINSAW)
        expected = 2
        actual = chainsaw.uses_remaining
        self.assertEqual(expected, actual)

        chainsaw.use()
        expected = 1
        actual = chainsaw.uses_remaining
        self.assertEqual(expected, actual)
    
    def test_combining_gasoline_and_chainsaw(self):
        chainsaw = get_item(ItemName.CHAINSAW)
        gasoline = get_item(ItemName.GASOLINE)
        chainsaw.use()
        chainsaw.use()

        expected = 0
        actual = chainsaw.uses_remaining
        self.assertEqual(expected, actual)

        expected = 1
        actual = gasoline.uses_remaining
        self.assertEqual(expected, actual)

        combine_items(chainsaw, gasoline)
        expected = 2
        actual = chainsaw.uses_remaining
        self.assertEqual(expected, actual)

        expected = 0
        actual = gasoline.uses_remaining
        self.assertEqual(expected, actual)