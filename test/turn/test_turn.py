import unittest
from unittest.mock import Mock, create_autospec

from src.model.turn import *

class TestTurn(unittest.TestCase):
    """tests for Turn (context and states"""
    def setUp(self):
        """set up a turn to test"""
        self.the_turn = Turn.create(*self.create_mock_services())

    @staticmethod
    def create_mock_services():
        """create mock services"""
        from src.model.interfaces import IPlayer, IGamePieces
        from src.view.mock_ui import UserInterface

        mock_player = create_autospec(IPlayer)
        mock_game_pieces = create_autospec(IGamePieces)
        mock_user_interface = create_autospec(UserInterface)

        return mock_game_pieces, mock_player, mock_user_interface


    def assert_pre_start(self):
        """Turn should start with no state"""
        self.assertTrue(self.the_turn.is_waiting_for_callback())
        with self.assertRaisesRegex(RuntimeError, "Cannot continue turn while waiting for input."):
            self.the_turn.continue_turn()

    def test_turn_before_start(self):
        """turn should start with no state"""
        self.assert_pre_start()


    def test_turn_after_start(self):
        """turn should be in the ready state"""
        self.the_turn.start_turn()
        self.assertEqual(self.the_turn._flow._current_state.name.value, 'ready')
        self.assertFalse(self.the_turn.is_waiting_for_callback())

    def test_continue_turn(self):
        """turn should move to the ready state then the get player tile state"""
        self.the_turn.start_turn()
        self.the_turn.continue_turn()
        self.assertEqual(self.the_turn._flow._current_state.name.value, 'get_player_tile')

    def test_turn_after_stop(self):
        """turn should move to pre_start with no state"""
        self.the_turn.start_turn()
        self.the_turn.continue_turn()
        self.the_turn.end_turn()
        self.assert_pre_start()


if __name__ == '__main__':
    unittest.main()
