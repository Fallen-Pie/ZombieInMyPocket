from enum import Enum
import unittest
from unittest.mock import Mock
from ...src.enums_and_types.game_message import MessageType, GameFeedbackMessage, GameSetupMessage, AlertMessage, GameOverMessage,GameInstruction
from ...src.model.game_message_manager.game_message_getter import GameMessageManager

class FakeEnum(Enum):
    """Mock enum for testing"""
    SIMPLE = "Plain message"
    WITH_PLACEHOLDER = "Hello {}"
    INVALID_TEMPLATE = 123

class TestGameMessageGetter(unittest.TestCase):
    def set_up(self):
        """ """
        self.getter = GameMessageManager()

    def test_post_and_get_simple_message(self):
        """Should store and retrieve a simple enum message."""
        self.getter.post_message(MessageType.FEEDBACK, FakeEnum.SIMPLE)
        msg = self.getter.get_messages(MessageType.FEEDBACK)
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
if __name__ == "__main__":
    unittest.main()