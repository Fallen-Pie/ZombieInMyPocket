import unittest
from src.model.player.player import Player


class TestHealthProperty(unittest.TestCase):
    """User Story: Health Property

    Given the player is in the game
    Then the player should have a health property with a default value
    """

    def setUp(self):
        self.player = Player()

    def test_health_damage_success(self):
        """Acceptance Criteria (Success):
        Given the player is damaged
        When the player's health is reduced
        Then the player's health value decreases accordingly
        """
        # Arrange
        damage_amount = 30
        expected_health = 70

        # Act
        self.player.take_damage(damage_amount)

        # Assert
        self.assertEqual(self.player.get_health(), expected_health)

    def test_health_excessive_damage_failure(self):
        """Acceptance Criteria (Failure):
        Given the player takes damage exceeding current health
        When health calculations are updated
        Then the player's health does not go below zero
        """
        # Arrange
        damage_amount = 150
        expected_health = 0

        # Act
        self.player.take_damage(damage_amount)

        # Assert
        self.assertEqual(self.player.get_health(), expected_health)
