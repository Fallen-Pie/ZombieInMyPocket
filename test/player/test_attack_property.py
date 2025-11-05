import unittest
from src.model.player.player import Player


class TestAttackProperty(unittest.TestCase):
    """User Story: Attack Property

    Given the player is in the game
    Then the player should have an attack property with a default value
    """

    def setUp(self):
        self.player = Player()

    def test_attack_power_deals_damage_success(self):
        """Acceptance Criteria (Success):
        Given the player has an attack property of 5
        When the player attacks an enemy
        Then the attack damage applied is 5
        """
        # Arrange
        player_with_attack_5 = Player(base_attack_power=5)
        expected_attack_power = 5

        # Act
        actual_attack_power = player_with_attack_5.get_attack_power()

        # Assert
        self.assertEqual(actual_attack_power, expected_attack_power)

    def test_attack_power_zero_deals_no_damage_failure(self):
        """Acceptance Criteria (Failure):
        Given the player's attack property is 0
        When the player attacks
        Then no damage is dealt to the target
        """
        # Arrange
        player_with_zero_attack = Player(base_attack_power=0)
        expected_attack_power = 0

        # Act
        actual_attack_power = player_with_zero_attack.get_attack_power()

        # Assert
        self.assertEqual(actual_attack_power, expected_attack_power)
