from enum import Enum
import unittest
from unittest.mock import Mock
from ...src.enums_and_types.game_message import MessageType, GameStateMessage, GameSetupMessage, AlertMessage, GameOverMessage,GameInstruction
from ...src.model.game_message_getter.game_message_getter import GameGameMessageGetter

class FakeEnum(Enum):
    """Mock enum for testing"""
    SIMPLE = "Plain message"
    WITH_PLACEHOLDER = "Hello {}"
    INVALID_TEMPLATE = 123

class TestGameMessageGetter(unittest.TestCase):
    def set_up(self):
        """ """
        self.getter = GameGameMessageGetter()

    def test_post_and_get_simple_message(self):
        """Should store and retrieve a simple enum message."""
        self.getter.post_message(MessageType.FEEDBACK, FakeEnum.SIMPLE)
        msg = self.getter.get_messages(MessageType.FEEDBACK, FakeEnum.SIMPLE)
        self.assertIn("A simple message", msg)

    def test_post_message_with_formatting(self):
        """Should correctly format the message."""
        self.getter.post_message(MessageType.STATUS, FakeEnum.WITH_PLACEHOLDER, "Player")
        msg = self.getter.get_messages(MessageType.STATUS)
        self.assertFalse(msg[0], "Hello Player")

    def test_post_message_not_enough_args_raises(self):
        """Should raise ValueError when not enough arguments are passed."""
        self.getter.post_message(MessageType.STATUS, FakeEnum.WITH_PLACEHOLDER)
        msg = self.getter.get_messages(MessageType.STATUS)
        self.assertIn("A simple message", msg)

    def test_post_message_with_invalid_template(self):
        """"""
        self.getter.post_message(MessageType.STATUS, FakeEnum.INVALID_TEMPLATE)
        msg = self.getter.get_messages(MessageType.STATUS)

    # def simulate_turn(message_getter):
    #     """Example game logic that posts messages for a turn."""
    #     message_getter.post_message(MessageType.GAME, GameCode.DRAW_CARD)
    #     message_getter.post_message(MessageType.GAME, GameCode.GRAB_ITEM, "Sword")
    #     message_getter.post_message(MessageType.STATUS, GameCode.HEALTH_DECREASE, -1)
    #     message_getter.post_message(MessageType.TIME, GameCode.TIME_PASS, "+1h")
    #
    # def test_turn_posts_expected_messages(mock_message_getter):
    #     # run turn simulation
    #     simulate_turn(mock_message_getter)
    #
    #     # check post_message calls
    #     mock_message_getter.post_message.assert_any_call(MessageType.GAME, GameCode.DRAW_CARD)
    #     mock_message_getter.post_message.assert_any_call(MessageType.GAME, GameCode.GRAB_ITEM, "Sword")
    #     mock_message_getter.post_message.assert_any_call(MessageType.STATUS, GameCode.HEALTH_DECREASE, -1)
    #     mock_message_getter.post_message.assert_any_call(MessageType.TIME, GameCode.TIME_PASS, "+1h")
    #
    #     # ensure total number of calls is correct
    #     assert mock_message_getter.post_message.call_count == 4
    #
    # def test_clear_messages(mock_message_getter):
    #     # simulate clearing messages
    #     mock_message_getter.clear_messages(MessageType.GAME)
    #     mock_message_getter.clear_messages.assert_called_once_with(MessageType.GAME)
    #
    # def test_get_messages(mock_message_getter):
    #     # stub return value
    #     mock_message_getter.get_messages.return_value = ["Player drew a card"]
    #     msgs = mock_message_getter.get_messages(MessageType.GAME)
    #
    #     assert msgs == ["Player drew a card"]
    #     mock_message_getter.get_messages.assert_called_once_with(MessageType.GAME)

if __name__ == "__main__":
    unittest.main()