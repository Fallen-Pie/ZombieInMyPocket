import unittest
from src.model.player.player import Player


class TestTotemTracking(unittest.TestCase):
    """User Story: Totem Tracking

    Given the player has a totem item
    When the player holds or picks up the totem
    Then the system should track that the player is holding the totem

    When the player drops the totem
    Then the system should track that the player is no longer holding the
    totem
    """

    def setUp(self):
        self.player = Player()

    def test_totem_pickup_success(self):
        """Acceptance Criteria (Success):
        Given the player picks up the totem
        When checked in the system
        Then the system shows the player is holding the totem
        """
        # Arrange
        self.assertFalse(self.player.has_totem())  # Initial state

        # Act
        self.player.set_has_totem(True)

        # Assert
        self.assertTrue(self.player.has_totem())

    def test_totem_drop_failure(self):
        """Acceptance Criteria (Failure):
        Given the player drops the totem
        When checked in the system
        Then the system shows the player does not have the totem
        """
        # Arrange
        self.player.set_has_totem(True)
        self.assertTrue(self.player.has_totem())  # Confirm initial state

        # Act
        self.player.set_has_totem(False)

        # Assert
        self.assertFalse(self.player.has_totem())
