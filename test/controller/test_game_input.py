import unittest
from unittest.mock import Mock, patch
from src.controller.game_controller import GameController
from src.common.interfaces.i_ui import IUI

class TestGameInput(unittest.TestCase):
    """User Story: Player Input Handling

    As a player, I want to be able to provide input to the game
    so that I can make choices and interact with the game world.
    """

    @patch('src.controller.game_controller.GameStatus')
    @patch('src.controller.game_controller.GameTime')
    @patch('src.controller.game_controller.Player')
    @patch('src.controller.game_controller.GamePieces')
    @patch('src.controller.game_controller.Turn')
    def setUp(self, MockTurn, MockGamePieces, MockPlayer, MockGameTime, MockGameStatus):
        """Set up the test environment for the GameController tests."""
        self.mock_ui = Mock(spec=IUI)
        self.game_controller = GameController()
        self.game_controller.ui = self.mock_ui
        self.game_controller.game_status = MockGameStatus()
        self.game_controller.the_turn = MockTurn()

    def test_handle_input_success(self):
        """Acceptance Criteria (Success):
        Given the game is waiting for player input
        When the player provides input
        Then the input is handled by the current turn state
        """
        # Arrange
        mock_state = Mock()
        mock_state.get_input_options.return_value = {"1": "Option 1"}
        mock_state.get_prompt.return_value = "Choose:"
        self.game_controller.the_turn._flow.current_state = mock_state
        self.mock_ui.get_input.return_value = "1"

        # Act
        self.game_controller._handle_input()

        # Assert
        self.mock_ui.get_input.assert_called_once_with("Choose:", {"1": "Option 1"})
        self.game_controller.the_turn._flow.handle_input.assert_called_once_with("1")
