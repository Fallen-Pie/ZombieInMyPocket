import unittest
from unittest.mock import Mock

from src.model.game_message_manager.game_feedback_manager import GameFeedbackManager
from src.enums_and_types.game_message import MessageType, GameFeedbackMessage, GameOverMessage, GameSetupMessage

class TestGameFeedbackManager(unittest.TestCase):
    def setUp(self):
        """ Mocking dependencies"""
        self.mock_msg_handler = Mock()
        self.mock_player = Mock()
        self.tile = Mock()

        self.manager = GameFeedbackManager(
            msg_handler=self.mock_msg_handler,
            tile=self.tile
        )
        # Reset call history at the start of each test
        self.mock_msg_handler.reset_mock()

    def test_on_game_state_change_posts_feedback(self):
        desc = "Player entered new phase"
        self.manager.on_game_state_change(desc)
        self.mock_msg_handler.post_message.assert_called_once_with(
            MessageType.FEEDBACK, MessageType.STATUS, desc
        )

    def test_on_time_change_posts_feedback(self):
        new_time = 45
        self.manager.on_time_change(new_time)
        self.mock_msg_handler.post_message.assert_called_once_with(
            MessageType.FEEDBACK, GameFeedbackMessage.TIME_CHANGE, new_time
        )

    def test_on_room_change_posts_feedback(self):
        room_name = "Graveyard"
        self.manager.on_room_change(room_name)
        self.mock_msg_handler.post_message.assert_called_once_with(
            MessageType.FEEDBACK, GameFeedbackMessage.ROOM_CHANGED, room_name
        )

    def test_on_item_acquired_posts_feedback(self):
        item = "Shotgun"
        self.manager.on_item_acquired(item)
        self.mock_msg_handler.post_message.assert_called_once_with(
            MessageType.FEEDBACK, GameFeedbackMessage.ITEM_ACQUIRED, item
        )

    def test_game_over_win_message(self):
        self.assertEqual(
            GameOverMessage.GAME_OVER_WIN.value,
            "Congratulations! You have won!"
        )

    def test_game_over_lose_time_message(self):
        self.assertEqual(
            GameOverMessage.GAME_OVER_LOSE_TIME.value,
            "Oh no. You ran out of time! You have been eaten by the zombies!"
        )

    def test_game_over_lose_health_message(self):
        self.assertEqual(
            GameOverMessage.GAME_OVER_LOSE_HEALTH.value,
            "Oh no. You are exhausted! You have been eaten by the zombies!"
        )

    def test_enum_members_are_unique(self):
        # Ensures no two values are duplicated
        values = [m.value for m in GameOverMessage]
        self.assertEqual(len(values), len(set(values)))

    def test_welcome_message_start_game(self):
        """
        🟢 Scenario (Basic Flow): Display Welcome Message at the start of the game - Current Room: Foyer
        •	Given the game has just started
        •	When the game pieces are initialized
        •	Then the player should see a welcome message
        •	And the current room tile should be displayed as “Foyer”
        """
        # self.room = "Foyer"
        # self.mock_player.room = "Foyer"
        # simulate stats display as welcome
        self.manager.on_game_start()
        self.mock_msg_handler.post_message.assert_called_once_with(
            MessageType.FEEDBACK, GameSetupMessage.GAME_START, "Foyer"
        )
        # # ensure STATUS messages are posted for all stats
        # self.assertEqual(self.mock_msg_handler.post_message.call_count,1)
        # self.mock_msg_handler.post_message.assert_any_call(
        #     MessageType.STATUS,
        #     unittest.mock.ANY
        # )

    def test_show_feedback_item_acquired(self):
        """
        🟡 Scenario (Alternate Flow) Display information that player acquired an item
        •	Given the player draw a next card
        •	When the item is obtained and collected
        •	Then a message should be displayed to confirm the item (and what) was acquired.
        """
        item: str = "Sword"
        self.manager.on_item_acquired(item)
        self.mock_msg_handler.post_message.assert_any_call(
            MessageType.FEEDBACK, unittest.mock.ANY
        )

if __name__ == '__main__':
    unittest.main()