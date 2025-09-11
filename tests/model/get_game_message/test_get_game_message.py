import unittest
from unittest.mock import Mock
from src.model.get_game_message import GetGameMessage
from src.enums_and_types.enums import GameStateMessage, GameSetupMessage, AlertMessage, GameOverMessage,GameInstruction,GameState

class TestGetGameMessage(unittest.TestCase):
    """ """
    # def test_get_game_message(self):
    #     pass

    def setUp(self):
        # Mock the ITime dependency
        mock_time = Mock()
        mock_time.get_time.return_value = 10  # fake time
        self.get_message = GetGameMessage()
        self.get_message.current_time = self.get_current_time(current_time=mock_time)

    def test_handle_game_over_win(self):
        result = self.get_message.handle_game_over("win event")
        self.assertEqual(result, GameOverMessage.GAME_OVER_WIN)

    def test_handle_game_over_lose_health(self):
        result = self.get_message.handle_game_over("lose event due to low health")
        self.assertEqual(result, GameOverMessage.GAME_OVER_LOSE_HEALTH)

    def test_handle_help_key_storage_room(self):
        result = self.get_message.handle_help_key("invalid cower move")
        self.assertEqual(result, GameInstruction.STORAGE_ROOM)

    def test_handle_warning_invalid_cower(self):
        result = self.get_message.handle_game_warning_event("invalid cower move", current_tile="tile1")
        self.assertEqual(result, AlertMessage.INVALID_COWER_MOVE)
