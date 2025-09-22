import unittest
from src.model.game_status.game_status import GameStatus
from src.enums_and_types.enums import MessageCode, GameOverConditions

class TestGameStatus(unittest.TestCase):

    def setUp(self):
        """Set up a new GameStatus instance before each test."""
        self.game_status = GameStatus()

    def test_initial_state(self):
        """Test that a new instance has the correct default values."""
        self.assertFalse(self.game_status.is_game_over)
        self.assertIsNone(self.game_status.game_over_condition)
        self.assertEqual(self.game_status.get_messages(), [])

    def test_post_message(self):
        """Test that posting a message adds it to the queue correctly."""
        self.game_status.post_message(MessageCode.ROOM_CHANGED, "Kitchen")
        messages = self.game_status.get_messages()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0], "Current Room Kitchen")

    def test_post_message_safe_formatting(self):
        """Test that posting a message with incorrect arguments fails gracefully."""
        # ROOM_CHANGED requires one argument, but we provide none.
        self.game_status.post_message(MessageCode.ROOM_CHANGED)
        messages = self.game_status.get_messages()
        self.assertEqual(len(messages), 1)
        self.assertIn("Error formatting message for code", messages[0])

    def test_trigger_game_over(self):
        """Test the game over trigger and condition."""
        self.game_status.trigger_game_over(GameOverConditions.LOSE_OUT_OF_TIME)
        self.assertTrue(self.game_status.is_game_over)
        self.assertEqual(self.game_status.game_over_condition, GameOverConditions.LOSE_OUT_OF_TIME)

    def test_message_queue(self):
        """Test that the message queue holds multiple messages in order."""
        self.game_status.post_message(MessageCode.WELCOME)
        self.game_status.post_message(MessageCode.LOW_HEALTH_WARNING)
        messages = self.game_status.get_messages()
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0], "Welcome")
        self.assertEqual(messages[1], "Low Health!")

    def test_clear_messages(self):
        """Test that the message queue can be cleared."""
        self.game_status.post_message(MessageCode.WELCOME)
        self.assertNotEqual(self.game_status.get_messages(), [])
        self.game_status.clear_messages()
        self.assertEqual(self.game_status.get_messages(), [])

    def test_reset(self):
        """Test that reset() puts the object back into its initial state."""
        # 1. Change the state
        self.game_status.post_message(MessageCode.WELCOME)
        self.game_status.trigger_game_over(GameOverConditions.LOSE_PLAYER_DIED)

        # 2. Verify the state is changed
        self.assertTrue(self.game_status.is_game_over)
        self.assertNotEqual(self.game_status.get_messages(), [])

        # 3. Reset the state
        self.game_status.reset()

        # 4. Verify it's back to the initial state
        self.assertFalse(self.game_status.is_game_over)
        self.assertIsNone(self.game_status.game_over_condition)
        self.assertEqual(self.game_status.get_messages(), [])

if __name__ == '__main__':
    unittest.main()
