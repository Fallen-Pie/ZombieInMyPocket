import unittest
from src.model.item.base_item import (
    BaseItem, ConsumableItem, WeaponItem,
    CombinableItem, SpecialWeaponItem
)
from src.enums_and_types import ItemName, ItemType


class TestBaseItem(unittest.TestCase):
    """Test class for BaseItem implementation details."""

    def test_base_item_initialization(self):
        # Arrange & Act
        item = BaseItem(
            name=ItemName.MACHETE,
            description="Test item",
            item_type=ItemType.WEAPON,
            attack_bonus=2,
            heal_amount=0,
            uses=5,
            combinable_with=[ItemName.OIL]
        )

        # Assert
        self.assertEqual(item.name, ItemName.MACHETE)
        self.assertEqual(item.description, "Test item")
        self.assertEqual(item.type, ItemType.WEAPON)
        self.assertEqual(item.attack_bonus, 2)
        self.assertEqual(item.heal_amount, 0)
        self.assertEqual(item.uses_remaining, 5)
        self.assertEqual(item.combinable_with, [ItemName.OIL])

    def test_base_item_use_decreases_uses(self):
        # Arrange
        item = BaseItem(
            name=ItemName.MACHETE,
            description="Test item",
            item_type=ItemType.WEAPON,
            uses=3
        )

        # Act
        should_be_discarded = item.use()

        # Assert
        self.assertFalse(should_be_discarded)
        self.assertEqual(item.uses_remaining, 2)

    def test_base_item_use_when_exhausted(self):
        # Arrange
        item = BaseItem(
            name=ItemName.MACHETE,
            description="Test item",
            item_type=ItemType.WEAPON,
            uses=1
        )

        # Act
        should_be_discarded = item.use()

        # Assert
        self.assertTrue(should_be_discarded)
        self.assertEqual(item.uses_remaining, 0)

    def test_base_item_use_when_already_exhausted(self):
        # Arrange
        item = BaseItem(
            name=ItemName.MACHETE,
            description="Test item",
            item_type=ItemType.WEAPON,
            uses=0
        )

        # Act
        should_be_discarded = item.use()

        # Assert
        self.assertTrue(should_be_discarded)
        self.assertEqual(item.uses_remaining, 0)

    def test_combinable_with_returns_copy(self):
        # Arrange
        original_list = [ItemName.OIL, ItemName.GASOLINE]
        item = BaseItem(
            name=ItemName.CANDLE,
            description="Test item",
            item_type=ItemType.COMBINE_ONLY,
            combinable_with=original_list
        )

        # Act
        returned_list = item.combinable_with
        returned_list.append(ItemName.CHAINSAW)

        # Assert
        self.assertEqual(len(item.combinable_with), 2)
        self.assertNotEqual(returned_list, item.combinable_with)


class TestConsumableItem(unittest.TestCase):
    """Test class for ConsumableItem implementation details."""

    def test_consumable_item_initialization(self):
        # Arrange & Act
        item = ConsumableItem(
            name=ItemName.CAN_OF_SODA,
            description="Healing item",
            item_type=ItemType.HEALING,
            heal_amount=3
        )

        # Assert
        self.assertEqual(item.name, ItemName.CAN_OF_SODA)
        self.assertEqual(item.type, ItemType.HEALING)
        self.assertEqual(item.heal_amount, 3)
        self.assertEqual(item.uses_remaining, 1)
        self.assertEqual(item.attack_bonus, 0)

    def test_consumable_item_with_combinable_items(self):
        # Arrange & Act
        item = ConsumableItem(
            name=ItemName.CAN_OF_SODA,
            description="Healing item",
            item_type=ItemType.HEALING,
            heal_amount=2,
            combinable_with=[ItemName.OIL]
        )

        # Assert
        self.assertEqual(item.combinable_with, [ItemName.OIL])


class TestWeaponItem(unittest.TestCase):
    """Test class for WeaponItem implementation details."""

    def test_weapon_item_initialization(self):
        # Arrange & Act
        item = WeaponItem(
            name=ItemName.MACHETE,
            description="Sharp weapon",
            attack_bonus=3,
            uses=10
        )

        # Assert
        self.assertEqual(item.name, ItemName.MACHETE)
        self.assertEqual(item.type, ItemType.WEAPON)
        self.assertEqual(item.attack_bonus, 3)
        self.assertEqual(item.uses_remaining, 10)
        self.assertEqual(item.heal_amount, 0)

    def test_weapon_item_default_uses(self):
        # Arrange & Act
        item = WeaponItem(
            name=ItemName.MACHETE,
            description="Sharp weapon",
            attack_bonus=2
        )

        # Assert
        self.assertEqual(item.uses_remaining, 99)

    def test_weapon_item_with_combinable_items(self):
        # Arrange & Act
        item = WeaponItem(
            name=ItemName.CHAINSAW,
            description="Loud weapon",
            attack_bonus=3,
            uses=2,
            combinable_with=[ItemName.GASOLINE]
        )

        # Assert
        self.assertEqual(item.combinable_with, [ItemName.GASOLINE])


class TestCombinableItem(unittest.TestCase):
    """Test class for CombinableItem implementation details."""

    def test_combinable_item_initialization(self):
        # Arrange & Act
        item = CombinableItem(
            name=ItemName.OIL,
            description="Slippery substance",
            item_type=ItemType.ESCAPE,
            combinable_with=[ItemName.CANDLE]
        )

        # Assert
        self.assertEqual(item.name, ItemName.OIL)
        self.assertEqual(item.type, ItemType.ESCAPE)
        self.assertEqual(item.uses_remaining, 1)
        self.assertEqual(item.combinable_with, [ItemName.CANDLE])
        self.assertEqual(item.attack_bonus, 0)
        self.assertEqual(item.heal_amount, 0)


class TestSpecialWeaponItem(unittest.TestCase):
    """Test class for SpecialWeaponItem implementation details."""

    def test_special_weapon_item_initialization(self):
        # Arrange & Act
        item = SpecialWeaponItem(
            name=ItemName.CHAINSAW,
            description="Motorized weapon",
            attack_bonus=3,
            uses=2,
            combinable_with=[ItemName.GASOLINE]
        )

        # Assert
        self.assertEqual(item.name, ItemName.CHAINSAW)
        self.assertEqual(item.type, ItemType.WEAPON)
        self.assertEqual(item.attack_bonus, 3)
        self.assertEqual(item.uses_remaining, 2)
        self.assertEqual(item.combinable_with, [ItemName.GASOLINE])

    def test_special_weapon_add_uses(self):
        # Arrange
        item = SpecialWeaponItem(
            name=ItemName.CHAINSAW,
            description="Motorized weapon",
            attack_bonus=3,
            uses=2
        )

        # Act
        item.add_uses(3)

        # Assert
        self.assertEqual(item.uses_remaining, 5)

    def test_special_weapon_add_uses_multiple_times(self):
        # Arrange
        item = SpecialWeaponItem(
            name=ItemName.CHAINSAW,
            description="Motorized weapon",
            attack_bonus=3,
            uses=1
        )

        # Act
        item.add_uses(2)
        item.add_uses(1)

        # Assert
        self.assertEqual(item.uses_remaining, 4)

    def test_special_weapon_use_and_add_uses(self):
        # Arrange
        item = SpecialWeaponItem(
            name=ItemName.CHAINSAW,
            description="Motorized weapon",
            attack_bonus=3,
            uses=2
        )

        # Act
        item.use()  # 2 -> 1
        item.add_uses(3)  # 1 -> 4
        item.use()  # 4 -> 3

        # Assert
        self.assertEqual(item.uses_remaining, 3)
