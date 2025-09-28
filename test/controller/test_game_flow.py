import unittest
from unittest.mock import Mock, patch
from src.controller.game_controller import GameController
from src.view.interfaces.i_ui import IUI
from src.enums_and_types.enums import MessageCode

class TestGameFlow(unittest.TestCase):
    """User Story: Game Flow Management

    As a player, I want the game to progress smoothly from one turn to the next
    so that I can have an uninterrupted gameplay experience.
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

    @patch('src.controller.game_controller.GameController.run_game')
    def test_begin_game_success(self, mock_run_game):
        """Acceptance Criteria (Success):
        Given the game is ready to start
        When the game begins
        Then a welcome message is posted and the main game loop is started
        """
        # Act
        self.game_controller.begin_game()

        # Assert
        self.game_controller.game_status.post_message.assert_called_once_with(MessageCode.WELCOME)
        mock_run_game.assert_called_once()

    def test_process_turn_success(self):
        """Acceptance Criteria (Success):
        Given the game is not waiting for player input
        When the turn is processed
        Then the game progresses to the next step in the turn
        """
        # Act
        self.game_controller._process_turn()

        # Assert
        self.game_controller.the_turn.continue_turn.assert_called_once()
