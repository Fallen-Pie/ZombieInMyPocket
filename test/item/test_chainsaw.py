from unittest import TestCase
from src.model.item.item_helper import IItem, get_item
from src.enums_and_types import ItemName, ItemType
from src.model.item.chainsaw import Chainsaw


class TestChainsaw(TestCase):

    def setUp(self):
        self._item: IItem = get_item(ItemName.CHAINSAW)

    def test_name_is_chainsaw(self):
        expected = ItemName.CHAINSAW
        actual = self._item.name
        self.assertEqual(expected, actual)

    def test_type_is_weapon(self):
        expected = ItemType.WEAPON
        actual = self._item.type
        self.assertEqual(expected, actual)

    def test_uses_is_two(self):
        expected = 2
        actual = self._item.uses_remaining
        self.assertEqual(expected, actual)

    def test_uses_is_one_after_use(self):
        self._item.use()
        expected = 1
        actual = self._item.uses_remaining
        self.assertEqual(expected, actual)

    def test_adding_uses_increases_uses(self):
        assert isinstance(self._item, Chainsaw)
        self._item.add_uses(2)
        expected = 4
        actual = self._item.uses_remaining
        self.assertEqual(expected, actual)

    def test_combinable_with_gasoline(self):
        expected = [ItemName.GASOLINE]
        actual = self._item.combinable_with
        self.assertEqual(expected, actual)

    def test_attack_bonus_is_three(self):
        expected = 3
        actual = self._item.attack_bonus
        self.assertEqual(expected, actual)
