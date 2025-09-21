# import pytest
from unittest.mock import Mock
from enum import Enum
from ...src.enums_and_types.game_message import MessageType
from ...src.model.game_message_getter.game_message_getter import GameMessageGetter
from ...src.enums_and_types.game_message import GameStateMessage, GameSetupMessage, AlertMessage, GameOverMessage,GameInstruction

class GameCode(Enum):
    DRAW_CARD = "Player drew a card"
    GRAB_ITEM = "Player grabbed an item"
    HEALTH_DECREASE = "Player lost health"
    TIME_PASS = "An hour has passed"

# @pytest.fixture
def mock_message_getter():
    """Fixture to mock IGameMessageGetter."""
    mock = Mock()
    mock.get_messages.return_value = []
    return mock

def simulate_turn(message_getter):
    """Example game logic that posts messages for a turn."""
    message_getter.post_message(MessageType.GAME, GameCode.DRAW_CARD)
    message_getter.post_message(MessageType.GAME, GameCode.GRAB_ITEM, "Sword")
    message_getter.post_message(MessageType.STATUS, GameCode.HEALTH_DECREASE, -1)
    message_getter.post_message(MessageType.TIME, GameCode.TIME_PASS, "+1h")

def test_turn_posts_expected_messages(mock_message_getter):
    # run turn simulation
    simulate_turn(mock_message_getter)

    # check post_message calls
    mock_message_getter.post_message.assert_any_call(MessageType.GAME, GameCode.DRAW_CARD)
    mock_message_getter.post_message.assert_any_call(MessageType.GAME, GameCode.GRAB_ITEM, "Sword")
    mock_message_getter.post_message.assert_any_call(MessageType.STATUS, GameCode.HEALTH_DECREASE, -1)
    mock_message_getter.post_message.assert_any_call(MessageType.TIME, GameCode.TIME_PASS, "+1h")

    # ensure total number of calls is correct
    assert mock_message_getter.post_message.call_count == 4

def test_clear_messages(mock_message_getter):
    # simulate clearing messages
    mock_message_getter.clear_messages(MessageType.GAME)
    mock_message_getter.clear_messages.assert_called_once_with(MessageType.GAME)

def test_get_messages(mock_message_getter):
    # stub return value
    mock_message_getter.get_messages.return_value = ["Player drew a card"]
    msgs = mock_message_getter.get_messages(MessageType.GAME)

    assert msgs == ["Player drew a card"]
    mock_message_getter.get_messages.assert_called_once_with(MessageType.GAME)
# class TestGetGameMessage(Enum):
#     """ """
    # def test_get_game_message(self):
    #     pass
    #
    # def setUp(self):
    #     # Mock the ITime dependency
    #     mock_time = Mock()
    #     mock_time.get_time.return_value = 10  # fake time
    #     self.get_message = GameMessageGetter()
    #     self.get_message.current_time = self.get_current_time(current_time=mock_time)
    #
    # def test_handle_game_over_win(self):
    #     result = self.get_message.handle_game_over("win event")
    #     self.assertEqual(result, GameOverMessage.GAME_OVER_WIN)
    #
    # def test_handle_game_over_lose_health(self):
    #     result = self.get_message.handle_game_over("lose event due to low health")
    #     self.assertEqual(result, GameOverMessage.GAME_OVER_LOSE_HEALTH)
    #
    # def test_handle_help_key_storage_room(self):
    #     result = self.get_message.handle_help_key("invalid cower move")
    #     self.assertEqual(result, GameInstruction.STORAGE_ROOM)
    #
    # def test_handle_warning_invalid_cower(self):
    #     result = self.get_message.handle_game_warning_event("invalid cower move", current_tile="tile1")
    #     self.assertEqual(result, AlertMessage.INVALID_COWER_MOVE)
