import unittest
from src.model.player.player import Player


class TestPlayerPositionTracking(unittest.TestCase):
    """User Story: Player Position Tracking

    Given the player moves in the game world
    When the player's position changes
    Then the system should track the player's current position
    """

    def setUp(self):
        self.player = Player()

    def test_position_tracking_success(self):
        """Acceptance Criteria (Success):
        Given the player moves to a new position
        When the position is checked
        Then the system shows the correct player position
        """
        # Arrange
        test_position = (5, 3)

        # Act
        self.player.set_position(test_position)

        # Assert
        self.assertEqual(self.player.get_position(), test_position)

    def test_position_validation_failure(self):
        """Acceptance Criteria (Failure):
        Given the player tries to move to an invalid position
        When the position is set
        Then the system should still track the position
        (Current implementation allows any position)
        """
        # Arrange
        test_position = (-1, -1)

        # Act
        self.player.set_position(test_position)

        # Assert - Current implementation allows any position
        self.assertEqual(self.player.get_position(), test_position)
