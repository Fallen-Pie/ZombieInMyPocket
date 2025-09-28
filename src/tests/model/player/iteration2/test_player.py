import unittest
from unittest.mock import Mock, patch
from src.model.player.iteration2.player import Player, PlayerImplementation
from src.enums_and_types.enums import ItemType
from src.model.interfaces.i_item import IItem

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.custom_player = Player(initial_health=50, initial_position=(5, 10), base_attack_power=3)

    def test_init_default_values(self):
        # Arrange
        # No setup needed
        
        # Act
        player = Player()
        
        # Assert
        self.assertEqual(player.get_health(), 100)
        self.assertEqual(player.get_position(), (0, 0))
        self.assertEqual(player.get_attack_power(), 1)

    def test_init_custom_values(self):
        # Arrange
        expected_health = 75
        expected_position = (3, 7)
        expected_attack_power = 5
        
        # Act
        player = Player(initial_health=expected_health, initial_position=expected_position, base_attack_power=expected_attack_power)
        
        # Assert
        self.assertEqual(player.get_health(), expected_health)
        self.assertEqual(player.get_position(), expected_position)
        self.assertEqual(player.get_attack_power(), expected_attack_power)

    def test_get_health(self):
        # Arrange
        expected_default_health = 100
        expected_custom_health = 50
        
        # Act
        default_health = self.player.get_health()
        custom_health = self.custom_player.get_health()
        
        # Assert
        self.assertEqual(default_health, expected_default_health)
        self.assertEqual(custom_health, expected_custom_health)

    def test_get_attack_power(self):
        # Arrange
        expected_default_attack_power = 1
        expected_custom_attack_power = 3
        
        # Act
        default_attack_power = self.player.get_attack_power()
        custom_attack_power = self.custom_player.get_attack_power()
        
        # Assert
        self.assertEqual(default_attack_power, expected_default_attack_power)
        self.assertEqual(custom_attack_power, expected_custom_attack_power)

    def test_get_position(self):
        # Arrange
        expected_default_position = (0, 0)
        expected_custom_position = (5, 10)
        
        # Act
        default_position = self.player.get_position()
        custom_position = self.custom_player.get_position()
        
        # Assert
        self.assertEqual(default_position, expected_default_position)
        self.assertEqual(custom_position, expected_custom_position)

    def test_set_position(self):
        # Arrange
        new_position = (10, 20)
        
        # Act
        self.player.set_position(new_position)
        
        # Assert
        self.assertEqual(self.player.get_position(), new_position)

    def test_get_inventory(self):
        # Arrange
        expected_inventory = []
        
        # Act
        inventory = self.player.get_inventory()
        
        # Assert
        self.assertEqual(inventory, expected_inventory)
        self.assertIsInstance(inventory, list)

    def test_take_damage(self):
        # Arrange
        damage_amount = 30
        expected_health = 70
        
        # Act
        self.player.take_damage(damage_amount)
        
        # Assert
        self.assertEqual(self.player.get_health(), expected_health)

    def test_heal(self):
        # Arrange
        heal_amount = 20
        expected_health = 120
        
        # Act
        self.player.heal(heal_amount)
        
        # Assert
        self.assertEqual(self.player.get_health(), expected_health)

    def test_has_totem(self):
        # Arrange
        expected_totem_status = False
        
        # Act
        has_totem = self.player.has_totem
        
        # Assert
        self.assertEqual(has_totem, expected_totem_status)

    def test_use_item(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type = ItemType.HEALING
        mock_item.heal_amount = 25
        mock_item.uses_remaining = 1
        self.player.add_item_to_inventory(mock_item)
        initial_health = self.player.get_health()
        
        # Act
        result = self.player.use_item(mock_item)
        
        # Assert
        self.assertEqual(self.player.get_health(), initial_health + 25)
        self.assertIsNone(result)

    def test_add_item_to_inventory(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        initial_inventory_length = len(self.player.get_inventory())
        
        # Act
        self.player.add_item_to_inventory(mock_item)
        
        # Assert
        self.assertEqual(len(self.player.get_inventory()), initial_inventory_length + 1)
        self.assertIn(mock_item, self.player.get_inventory())

    def test_remove_item_from_inventory(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player.add_item_to_inventory(mock_item)
        initial_inventory_length = len(self.player.get_inventory())
        
        # Act
        self.player.remove_item_from_inventory(mock_item)
        
        # Assert
        self.assertEqual(len(self.player.get_inventory()), initial_inventory_length - 1)
        self.assertNotIn(mock_item, self.player.get_inventory())

    def test_combine_items_from_inventory(self):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item1.name = "ItemA"
        mock_item1.uses_remaining = 1
        mock_item2 = Mock(spec=IItem)
        mock_item2.name = "ItemB"
        mock_item2.uses_remaining = 1
        mock_item2.combinable_with = ["ItemA"]
        self.player.add_item_to_inventory(mock_item1)
        self.player.add_item_to_inventory(mock_item2)
        
        # Act
        result = self.player.combine_items_from_inventory()
        
        # Assert
        self.assertIsInstance(result, bool)


class TestPlayerImplementation(unittest.TestCase):

    def setUp(self):
        self.player_impl = PlayerImplementation(initial_health=100, initial_position=(0, 0), base_attack_power=1)
        self.custom_player_impl = PlayerImplementation(initial_health=50, initial_position=(5, 10), base_attack_power=3)

    def test_init(self):
        # Arrange
        expected_health = 75
        expected_position = (3, 7)
        expected_attack_power = 5
        expected_inventory = []
        expected_has_totem = False
        
        # Act
        impl = PlayerImplementation(expected_health, expected_position, expected_attack_power)
        
        # Assert
        self.assertEqual(impl.health, expected_health)
        self.assertEqual(impl.position, expected_position)
        self.assertEqual(impl.attack_power, expected_attack_power)
        self.assertEqual(impl.inventory, expected_inventory)
        self.assertEqual(impl.has_totem, expected_has_totem)

    def test_health_property(self):
        # Arrange
        expected_default_health = 100
        expected_custom_health = 50
        
        # Act
        default_health = self.player_impl.health
        custom_health = self.custom_player_impl.health
        
        # Assert
        self.assertEqual(default_health, expected_default_health)
        self.assertEqual(custom_health, expected_custom_health)

    def test_attack_power_property(self):
        # Arrange
        expected_default_attack_power = 1
        expected_custom_attack_power = 3
        
        # Act
        default_attack_power = self.player_impl.attack_power
        custom_attack_power = self.custom_player_impl.attack_power
        
        # Assert
        self.assertEqual(default_attack_power, expected_default_attack_power)
        self.assertEqual(custom_attack_power, expected_custom_attack_power)

    def test_has_totem_property(self):
        # Arrange
        expected_has_totem = False
        
        # Act
        has_totem = self.player_impl.has_totem
        
        # Assert
        self.assertEqual(has_totem, expected_has_totem)

    def test_inventory_property_returns_copy(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory.append(mock_item)
        expected_original_length = 1
        
        # Act
        inventory_copy = self.player_impl.inventory
        inventory_copy.clear()
        
        # Assert
        self.assertEqual(len(inventory_copy), 0)
        self.assertEqual(len(self.player_impl._inventory), expected_original_length)

    def test_position_property_getter(self):
        # Arrange
        expected_default_position = (0, 0)
        expected_custom_position = (5, 10)
        
        # Act
        default_position = self.player_impl.position
        custom_position = self.custom_player_impl.position
        
        # Assert
        self.assertEqual(default_position, expected_default_position)
        self.assertEqual(custom_position, expected_custom_position)

    def test_position_property_setter(self):
        # Arrange
        new_position = (15, 25)
        
        # Act
        self.player_impl.position = new_position
        
        # Assert
        self.assertEqual(self.player_impl.position, new_position)

    def test_take_damage_normal(self):
        # Arrange
        damage_amount = 30
        expected_health = 70
        
        # Act
        self.player_impl.take_damage(damage_amount)
        
        # Assert
        self.assertEqual(self.player_impl.health, expected_health)

    def test_take_damage_excessive(self):
        # Arrange
        damage_amount = 150
        expected_health = 0
        
        # Act
        self.player_impl.take_damage(damage_amount)
        
        # Assert
        self.assertEqual(self.player_impl.health, expected_health)

    def test_take_damage_zero(self):
        # Arrange
        damage_amount = 0
        expected_health = 100
        
        # Act
        self.player_impl.take_damage(damage_amount)
        
        # Assert
        self.assertEqual(self.player_impl.health, expected_health)

    def test_heal(self):
        # Arrange
        initial_health = 50
        heal_amount = 30
        expected_health = 80
        self.player_impl._health = initial_health
        
        # Act
        self.player_impl.heal(heal_amount)
        
        # Assert
        self.assertEqual(self.player_impl.health, expected_health)

    def test_heal_zero(self):
        # Arrange
        heal_amount = 0
        original_health = self.player_impl.health
        
        # Act
        self.player_impl.heal(heal_amount)
        
        # Assert
        self.assertEqual(self.player_impl.health, original_health)

    def test_use_item_healing_type(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type = ItemType.HEALING
        mock_item.heal_amount = 25
        mock_item.uses_remaining = 1
        initial_health = 75
        expected_health = 100
        expected_result = None
        
        self.player_impl._inventory = [mock_item]
        self.player_impl._health = initial_health
        
        # Act
        result = self.player_impl.use_item(mock_item)
        
        # Assert
        self.assertEqual(self.player_impl.health, expected_health)
        self.assertEqual(result, expected_result)

    def test_use_item_weapon_type(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type = ItemType.WEAPON
        mock_item.attack_bonus = 5
        mock_item.uses_remaining = 1
        expected_result = 6  # base_attack_power (1) + attack_bonus (5)
        
        self.player_impl._inventory = [mock_item]
        
        # Act
        result = self.player_impl.use_item(mock_item)
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_use_item_removes_when_no_uses_remaining(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type = ItemType.HEALING
        mock_item.heal_amount = 25
        mock_item.uses_remaining = 0
        expected_inventory_length = 0
        
        self.player_impl._inventory = [mock_item]
        
        # Act
        self.player_impl.use_item(mock_item)
        
        # Assert
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)

    def test_use_item_not_in_inventory(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1
        mock_item.heal_amount = 25
        expected_result = None
        expected_health = 100
        
        # Act
        result = self.player_impl.use_item(mock_item)
        
        # Assert
        self.assertEqual(result, expected_result)
        self.assertEqual(self.player_impl.health, expected_health)

    def test_use_item_other_type(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type = ItemType.COMBINE_ONLY
        mock_item.uses_remaining = 1
        expected_result = None
        
        self.player_impl._inventory = [mock_item]
        
        # Act
        result = self.player_impl.use_item(mock_item)
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_add_item_to_inventory_under_limit(self):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        expected_length_after_first = 1
        expected_length_after_second = 2
        
        # Act
        self.player_impl.add_item_to_inventory(mock_item1)
        length_after_first = len(self.player_impl._inventory)
        
        self.player_impl.add_item_to_inventory(mock_item2)
        length_after_second = len(self.player_impl._inventory)
        
        # Assert
        self.assertEqual(length_after_first, expected_length_after_first)
        self.assertEqual(length_after_second, expected_length_after_second)

    def test_add_item_to_inventory_at_limit(self):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        mock_item3 = Mock(spec=IItem)
        expected_inventory_length = 2
        
        # Act
        self.player_impl.add_item_to_inventory(mock_item1)
        self.player_impl.add_item_to_inventory(mock_item2)
        self.player_impl.add_item_to_inventory(mock_item3)  # Should not be added
        
        # Assert
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)
        self.assertNotIn(mock_item3, self.player_impl._inventory)

    def test_remove_item_from_inventory_item_exists(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item]
        expected_inventory_length = 0
        
        # Act
        self.player_impl.remove_item_from_inventory(mock_item)
        
        # Assert
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)

    def test_remove_item_from_inventory_item_not_exists(self):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item1]
        expected_inventory_length = 1
        
        # Act
        self.player_impl.remove_item_from_inventory(mock_item2)
        
        # Assert
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)
        self.assertIn(mock_item1, self.player_impl._inventory)

    @patch('src.model.player.iteration2.player.combine_items')
    def test_combine_items_from_inventory_success(self, mock_combine_items):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 0
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 1
        expected_result = True
        expected_inventory_length = 1
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.return_value = expected_result
        
        # Act
        result = self.player_impl.combine_items_from_inventory()
        
        # Assert
        self.assertEqual(result, expected_result)
        mock_combine_items.assert_called_once_with(mock_item1, mock_item2)
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)
        self.assertNotIn(mock_item1, self.player_impl._inventory)
        self.assertIn(mock_item2, self.player_impl._inventory)

    @patch('src.model.player.iteration2.player.combine_items')
    def test_combine_items_from_inventory_both_items_depleted(self, mock_combine_items):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 0
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 0
        expected_result = True
        expected_inventory_length = 0
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.return_value = expected_result
        
        # Act
        result = self.player_impl.combine_items_from_inventory()
        
        # Assert
        self.assertEqual(result, expected_result)
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)

    @patch('src.model.player.iteration2.player.combine_items')
    def test_combine_items_from_inventory_assertion_error(self, mock_combine_items):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 1
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 1
        expected_result = False
        expected_inventory_length = 2
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.side_effect = AssertionError("Cannot combine these items")
        
        # Act
        result = self.player_impl.combine_items_from_inventory()
        
        # Assert
        self.assertEqual(result, expected_result)
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)

    def test_combine_items_from_inventory_less_than_two_items(self):
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item]
        expected_result = False
        
        # Act
        result = self.player_impl.combine_items_from_inventory()
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_combine_items_from_inventory_empty_inventory(self):
        # Arrange
        expected_result = False
        
        # Act
        result = self.player_impl.combine_items_from_inventory()
        
        # Assert
        self.assertEqual(result, expected_result)

    @patch('src.model.player.iteration2.player.combine_items')
    def test_combine_items_from_inventory_no_items_depleted(self, mock_combine_items):
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 2
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 3
        expected_result = True
        expected_inventory_length = 2
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.return_value = expected_result
        
        # Act
        result = self.player_impl.combine_items_from_inventory()
        
        # Assert
        self.assertEqual(result, expected_result)
        self.assertEqual(len(self.player_impl._inventory), expected_inventory_length)


if __name__ == '__main__':
    unittest.main()