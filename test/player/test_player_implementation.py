import unittest
from unittest.mock import Mock, patch
from src.model.player.player import Player, _PlayerImplementation
from src.model.interfaces.i_item import IItem


class Test_PlayerImplementation(unittest.TestCase):
    """Test class for _PlayerImplementation internal logic."""

    def setUp(self):
        self.player_impl = _PlayerImplementation(
            initial_health=100,
            initial_position=(0, 0),
            base_attack_power=1
        )
        self.custom_player_impl = _PlayerImplementation(
            initial_health=80,
            initial_position=(5, 10),
            base_attack_power=3
        )

    def test_init(self):
        """Test _PlayerImplementation initialization."""
        # Assert default values
        self.assertEqual(self.player_impl.health, 100)
        self.assertEqual(self.player_impl.attack_power, 1)
        self.assertEqual(self.player_impl.position, (0, 0))
        self.assertEqual(len(self.player_impl.inventory), 0)
        self.assertEqual(self.player_impl.has_totem, False)

        # Assert custom values
        self.assertEqual(self.custom_player_impl.health, 80)
        self.assertEqual(self.custom_player_impl.attack_power, 3)
        self.assertEqual(self.custom_player_impl.position, (5, 10))

    def test_health_property(self):
        """Test health property accessor."""
        # Assert
        self.assertEqual(self.player_impl.health, 100)
        self.assertEqual(self.custom_player_impl.health, 80)

    def test_attack_power_property(self):
        """Test attack_power property accessor."""
        # Assert
        self.assertEqual(self.player_impl.attack_power, 1)
        self.assertEqual(self.custom_player_impl.attack_power, 3)

    def test_has_totem_property(self):
        """Test totem property accessor."""
        # Assert
        self.assertEqual(self.player_impl.has_totem, False)

    def test_inventory_property_returns_copy(self):
        """Test inventory property returns copy to prevent modification."""
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory.append(mock_item)
        expected_original_length = 1

        # Act
        inventory_copy = self.player_impl.inventory
        inventory_copy.clear()

        # Assert
        self.assertEqual(len(inventory_copy), 0)
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_original_length
        )

    def test_position_property_getter(self):
        """Test position property getter."""
        # Assert
        self.assertEqual(self.player_impl.position, (0, 0))
        self.assertEqual(self.custom_player_impl.position, (5, 10))

    def test_position_property_setter(self):
        """Test position property setter."""
        # Arrange
        new_position = (15, 25)

        # Act
        self.player_impl.position = new_position

        # Assert
        self.assertEqual(self.player_impl.position, new_position)

    def test_take_damage_normal(self):
        """Test normal damage application."""
        # Arrange
        damage_amount = 30
        expected_health = 70

        # Act
        self.player_impl.take_damage(damage_amount)

        # Assert
        self.assertEqual(self.player_impl.health, expected_health)

    def test_take_damage_excessive(self):
        """Test excessive damage doesn't go below zero."""
        # Arrange
        damage_amount = 150
        expected_health = 0

        # Act
        self.player_impl.take_damage(damage_amount)

        # Assert
        self.assertEqual(self.player_impl.health, expected_health)

    def test_take_damage_zero(self):
        """Test zero damage has no effect."""
        # Arrange
        damage_amount = 0
        expected_health = 100

        # Act
        self.player_impl.take_damage(damage_amount)

        # Assert
        self.assertEqual(self.player_impl.health, expected_health)

    def test_heal(self):
        """Test healing functionality."""
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
        """Test zero healing has no effect."""
        # Arrange
        heal_amount = 0
        original_health = self.player_impl.health

        # Act
        self.player_impl.heal(heal_amount)

        # Assert
        self.assertEqual(self.player_impl.health, original_health)

    def test_use_item_healing_type(self):
        """Test using healing items."""
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1  # HEALING
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
        """Test using weapon items."""
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 0  # WEAPON
        mock_item.attack_bonus = 5
        mock_item.uses_remaining = 1
        expected_result = 6  # base_attack_power (1) + attack_bonus (5)

        self.player_impl._inventory = [mock_item]

        # Act
        result = self.player_impl.use_item(mock_item)

        # Assert
        self.assertEqual(result, expected_result)

    def test_use_item_removes_when_no_uses_remaining(self):
        """Test item removal when uses_remaining is 0."""
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1  # HEALING
        mock_item.heal_amount = 25
        mock_item.uses_remaining = 0
        expected_inventory_length = 0

        self.player_impl._inventory = [mock_item]

        # Act
        self.player_impl.use_item(mock_item)

        # Assert
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )

    def test_use_item_not_in_inventory(self):
        """Test using item not in inventory has no effect."""
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
        """Test using items of other types."""
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 2  # Neither HEALING nor WEAPON
        mock_item.uses_remaining = 1
        expected_result = None

        self.player_impl._inventory = [mock_item]

        # Act
        result = self.player_impl.use_item(mock_item)

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_item_to_inventory_under_limit(self):
        """Test adding items under inventory limit."""
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
        """Test adding items at inventory limit."""
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        mock_item3 = Mock(spec=IItem)
        expected_inventory_length = 2

        # Act
        self.player_impl.add_item_to_inventory(mock_item1)
        self.player_impl.add_item_to_inventory(mock_item2)
        # Should not be added:
        self.player_impl.add_item_to_inventory(mock_item3)

        # Assert
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )
        self.assertNotIn(mock_item3, self.player_impl._inventory)

    def test_remove_item_from_inventory_item_exists(self):
        """Test removing existing item from inventory."""
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item]
        expected_inventory_length = 0

        # Act
        self.player_impl.remove_item_from_inventory(mock_item)

        # Assert
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )

    def test_remove_item_from_inventory_item_not_exists(self):
        """Test removing non-existent item from inventory."""
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item1]
        expected_inventory_length = 1

        # Act
        self.player_impl.remove_item_from_inventory(mock_item2)

        # Assert
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )
        self.assertIn(mock_item1, self.player_impl._inventory)

    @patch('src.model.player.player.combine_items')
    def test_combine_items_from_inventory_success(self, mock_combine_items):
        """Test successful item combination."""
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
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )
        self.assertNotIn(mock_item1, self.player_impl._inventory)
        self.assertIn(mock_item2, self.player_impl._inventory)

    @patch('src.model.player.player.combine_items')
    def test_combine_items_from_inventory_both_items_depleted(
        self,
        mock_combine_items
    ):
        """Test combination when both items are depleted."""
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
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )

    @patch('src.model.player.player.combine_items')
    def test_combine_items_from_inventory_assertion_error(
        self,
        mock_combine_items
    ):
        """Test combination failure due to AssertionError."""
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 1
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 1
        expected_result = False
        expected_inventory_length = 2

        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.side_effect = AssertionError(
            "Cannot combine these items"
        )

        # Act
        result = self.player_impl.combine_items_from_inventory()

        # Assert
        self.assertEqual(result, expected_result)
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )

    def test_combine_items_from_inventory_less_than_two_items(self):
        """Test combination with insufficient items."""
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item]
        expected_result = False

        # Act
        result = self.player_impl.combine_items_from_inventory()

        # Assert
        self.assertEqual(result, expected_result)

    def test_combine_items_from_inventory_empty_inventory(self):
        """Test combination with empty inventory."""
        # Arrange
        expected_result = False

        # Act
        result = self.player_impl.combine_items_from_inventory()

        # Assert
        self.assertEqual(result, expected_result)

    def test_combine_items_from_inventory_no_items_depleted(self):
        """Test combination when no items are depleted."""
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 1
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 1
        expected_inventory_length = 2

        self.player_impl._inventory = [mock_item1, mock_item2]

        # Act
        with patch('src.model.player.player.combine_items',
                   return_value=True):
            self.player_impl.combine_items_from_inventory()

        # Assert
        self.assertEqual(
            len(self.player_impl._inventory),
            expected_inventory_length
        )
        self.assertIn(mock_item1, self.player_impl._inventory)
        self.assertIn(mock_item2, self.player_impl._inventory)

    def test_set_totem_functionality(self):
        """Test set_has_totem method functionality."""
        # Arrange
        initial_state = False
        self.assertEqual(self.player_impl.has_totem, initial_state)

        # Act
        self.player_impl.set_has_totem(True)

        # Assert
        self.assertTrue(self.player_impl.has_totem)

        # Act again
        self.player_impl.set_has_totem(False)

        # Assert
        self.assertFalse(self.player_impl.has_totem)

    def test_combat_with_gasoline_and_candle(self):
        """Test complex combat scenario with gasoline and candle."""
        # Arrange
        mock_gasoline = Mock(spec=IItem)
        mock_gasoline.name = "Gasoline"
        mock_gasoline.type.value = 2  # SPECIAL/OTHER type
        mock_gasoline.uses_remaining = 0  # Will be removed after use

        mock_candle = Mock(spec=IItem)
        mock_candle.name = "Candle"
        mock_candle.type.value = 2  # SPECIAL/OTHER type
        mock_candle.uses_remaining = 3

        initial_health = 80
        self.player_impl._health = initial_health
        self.player_impl._inventory = [mock_gasoline, mock_candle]

        # Act - Simulate using gasoline and candle together in combat
        gasoline_result = self.player_impl.use_item(mock_gasoline)
        candle_result = self.player_impl.use_item(mock_candle)

        # Assert
        # All zombies killed (simulated by successful item usage)
        self.assertIsNone(gasoline_result)
        self.assertIsNone(candle_result)

        # Gasoline removed from inventory (uses_remaining = 0, depleted)
        self.assertNotIn(mock_gasoline, self.player_impl._inventory)

        # Candle remains in inventory (uses_remaining = 3, still usable)
        self.assertIn(mock_candle, self.player_impl._inventory)

        # Player health unaffected
        self.assertEqual(self.player_impl.health, initial_health)


class TestPlayer(unittest.TestCase):
    """Test class for Player facade/API functionality."""

    def setUp(self):
        self.player = Player()
        self.custom_player = Player(
            initial_health=50,
            initial_position=(5, 10),
            base_attack_power=3
        )

    def test_init_default_values(self):
        """Test Player initialization with default values."""
        # Act
        player = Player()

        # Assert
        self.assertEqual(player.get_health(), 100)
        self.assertEqual(player.get_position(), (0, 0))
        self.assertEqual(player.get_attack_power(), 1)

    def test_init_custom_values(self):
        """Test Player initialization with custom values."""
        # Arrange
        expected_health = 75
        expected_position = (3, 7)
        expected_attack_power = 5

        # Act
        player = Player(
            initial_health=expected_health,
            initial_position=expected_position,
            base_attack_power=expected_attack_power
        )

        # Assert
        self.assertEqual(player.get_health(), expected_health)
        self.assertEqual(player.get_position(), expected_position)
        self.assertEqual(player.get_attack_power(), expected_attack_power)

    def test_get_health(self):
        """Test health getter methods."""
        # Assert
        self.assertEqual(self.player.get_health(), 100)
        self.assertEqual(self.custom_player.get_health(), 50)

    def test_get_attack_power(self):
        """Test attack power getter methods."""
        # Assert
        self.assertEqual(self.player.get_attack_power(), 1)
        self.assertEqual(self.custom_player.get_attack_power(), 3)

    def test_get_position(self):
        """Test position getter methods."""
        # Assert
        self.assertEqual(self.player.get_position(), (0, 0))
        self.assertEqual(self.custom_player.get_position(), (5, 10))

    def test_set_position(self):
        """Test position setter method."""
        # Arrange
        new_position = (10, 20)

        # Act
        self.player.set_position(new_position)

        # Assert
        self.assertEqual(self.player.get_position(), new_position)

    def test_get_inventory(self):
        """Test inventory getter method."""
        # Assert
        self.assertEqual(self.player.get_inventory(), [])
        self.assertIsInstance(self.player.get_inventory(), list)

    def test_take_damage(self):
        """Test damage functionality."""
        # Arrange
        damage_amount = 30
        expected_health = 70

        # Act
        self.player.take_damage(damage_amount)

        # Assert
        self.assertEqual(self.player.get_health(), expected_health)

    def test_heal(self):
        """Test healing functionality."""
        # Arrange
        heal_amount = 20
        expected_health = 120

        # Act
        self.player.heal(heal_amount)

        # Assert
        self.assertEqual(self.player.get_health(), expected_health)

    def test_has_totem_default(self):
        """Test totem tracking defaults to False."""
        # Assert
        self.assertEqual(self.player.has_totem(), False)

    def test_use_item(self):
        """Test basic item usage functionality."""
        # Arrange
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1  # HEALING
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
        """Test adding items to inventory."""
        # Arrange
        mock_item = Mock(spec=IItem)
        initial_inventory_length = len(self.player.get_inventory())

        # Act
        self.player.add_item_to_inventory(mock_item)

        # Assert
        self.assertEqual(
            len(self.player.get_inventory()),
            initial_inventory_length + 1
        )
        self.assertIn(mock_item, self.player.get_inventory())

    def test_remove_item_from_inventory(self):
        """Test removing items from inventory."""
        # Arrange
        mock_item = Mock(spec=IItem)
        self.player.add_item_to_inventory(mock_item)
        initial_inventory_length = len(self.player.get_inventory())

        # Act
        self.player.remove_item_from_inventory(mock_item)

        # Assert
        self.assertEqual(
            len(self.player.get_inventory()),
            initial_inventory_length - 1
        )
        self.assertNotIn(mock_item, self.player.get_inventory())

    def test_remove_item_not_in_inventory(self):
        """Test removing item that doesn't exist in inventory."""
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        self.player.add_item_to_inventory(mock_item1)
        expected_inventory_length = 1

        # Act
        self.player.remove_item_from_inventory(mock_item2)

        # Assert
        self.assertEqual(
            len(self.player.get_inventory()),
            expected_inventory_length
        )
        self.assertIn(mock_item1, self.player.get_inventory())

    def test_combine_items_from_inventory(self):
        """Test basic item combination functionality."""
        # Arrange
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        mock_item1.name = "item1"
        mock_item2.name = "item2"
        mock_item1.combinable_with = ["item2"]
        mock_item2.combinable_with = ["item1"]
        self.player.add_item_to_inventory(mock_item1)
        self.player.add_item_to_inventory(mock_item2)

        # Act
        result = self.player.combine_items_from_inventory()

        # Assert
        self.assertIsInstance(result, bool)
