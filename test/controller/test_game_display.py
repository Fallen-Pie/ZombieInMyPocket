import unittest
from unittest.mock import Mock, patch
from src.controller.game_controller import GameController
from src.view.interfaces.i_ui import IUI
from src.model.turn.turn_common import ServiceNames

class TestGameDisplay(unittest.TestCase):
    """User Story: Game State Display

    As a player, I want to see the current state of the game
    so that I can make informed decisions.
    """

    @patch('src.controller.game_controller.GameStatus')
    @patch('src.controller.game_controller.GameTime')
    @patch('src.controller.game_controller.Player')
    @patch('src.controller.game_controller.GamePieces')
    @patch('src.controller.game_controller.Turn')
    def setUp(self, MockTurn, MockGamePieces, MockPlayer, MockGameTime, MockGameStatus):
        """Set up the test environment for the GameController tests."""
        self.mock_ui = Mock(spec=IUI)
        self.game_controller = GameController(self.mock_ui)
        self.game_controller.game_status = MockGameStatus()
        self.game_controller.the_turn = MockTurn()

    def test_process_and_display_messages_success(self):
        """Acceptance Criteria (Success):
        Given there are messages in the game status
        When the messages are processed
        Then they are displayed on the UI and cleared from the status
        """
        # Arrange
        messages = ["msg1", "msg2"]
        self.game_controller.game_status.get_messages.return_value = messages

        # Act
        self.game_controller._process_and_display_messages()

        # Assert
        self.mock_ui.display_message.assert_any_call("msg1")
        self.mock_ui.display_message.assert_any_call("msg2")
        self.assertEqual(self.mock_ui.display_message.call_count, 2)
        self.game_controller.game_status.clear_messages.assert_called_once()

    def test_update_full_state_success(self):
        """Acceptance Criteria (Success):
        Given the game state has changed
        When the display is updated
        Then the UI shows the correct player and tile information
        """
        # Arrange
        mock_player = Mock()
        mock_player.get_health.return_value = 80
        mock_player.get_attack_power.return_value = 5
        mock_item = Mock()
        mock_item.name = "item1"
        mock_player.get_inventory.return_value = [mock_item]
        mock_player.get_position.return_value = (1, 1)

        mock_game_pieces = Mock()
        mock_tile = Mock()
        mock_game_pieces.get_tile.return_value = mock_tile
        mock_game_pieces.get_tile_position.return_value = (1, 1)

        self.game_controller.the_turn._flow._services = {
            ServiceNames.PLAYER: mock_player,
            ServiceNames.GAME_PIECES: mock_game_pieces
        }
        
        # Act
        self.game_controller._update_full_state()

        # Assert
        self.mock_ui.display_game_state.assert_called_once_with(
            tile=mock_tile,
            tile_position=(1, 1)
        )
        self.mock_ui.display_player_state.assert_called_once_with(
            player_health=80,
            player_attack=5,
            items=["item1"]
        )
