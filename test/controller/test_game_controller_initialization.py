import unittest
from unittest.mock import Mock, patch
from src.controller.game_controller import GameController
from src.view.interfaces.i_ui import IUI

class TestGameControllerInitialization(unittest.TestCase):
    """User Story: Game Controller Initialization

    As a developer, I want the game controller to be initialized correctly
    so that all its dependencies are in place for the game to start.
    """

    @patch('src.controller.game_controller.GameStatus')
    @patch('src.controller.game_controller.GameTime')
    @patch('src.controller.game_controller.Player')
    @patch('src.controller.game_controller.GamePieces')
    @patch('src.controller.game_controller.Turn')
    def test_initialization_success(self, MockTurn, MockGamePieces, MockPlayer, MockGameTime, MockGameStatus):
        """Acceptance Criteria (Success):
        Given the game is starting
        When the GameController is initialized
        Then all its components are created
        """
        # Arrange
        mock_ui = Mock(spec=IUI)

        # Act
        game_controller = GameController(mock_ui)

        # Assert
        MockGameStatus.assert_called_once()
        MockGameTime.assert_called_once()
        MockPlayer.assert_called_once()
        MockGamePieces.assert_called_once()
        MockTurn.create.assert_called_once_with(
            MockGamePieces(), MockPlayer(), mock_ui
        )
        self.assertIsNotNone(game_controller.game_status)
        self.assertIsNotNone(game_controller.the_turn)
        self.assertEqual(game_controller.ui, mock_ui)
