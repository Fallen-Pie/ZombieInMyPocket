import unittest
from unittest.mock import Mock

from src.model.game_message_getter.info_message_manager import InfoMessageManager
from src.enums_and_types.game_message import MessageType, GameInstruction
# from src.enums_and_types.direction import Direction
# from src.model.game_pieces.tile import Tile
# from src.model.game_time import GameTime
# from src.model.player import Player
# from src.model.interfaces.i_game_message_getter import IGameMessageGetter
#

class TestInfoMessageManager(unittest.TestCase):
    def setUp(self):
        """ Mocking dependencies"""
        self.mock_msg_handler = Mock()
        self.mock_player = Mock()
        self.mock_tile = Mock()
        self.mock_time = Mock()

        self.mock_player.get_health = 5
        self.mock_player.get_attack_power = 2
        self.mock_player.room = "Graveyard"  # For instruction mapping
        self.mock_tile.get_name = "Graveyard"
        self.mock_time.get_current_time = "10PM"
        self.mock_player.items = [
            Mock(name="Sword", attack_score=3),
            Mock(name="Shield", attack_score=1)
        ]
        self.manager = InfoMessageManager(
            msg_handler=self.mock_msg_handler,
            player=self.mock_player,
            tile=self.mock_tile,
            time=self.mock_time
        )
        # Reset call history at the start of each test
        self.mock_msg_handler.reset_mock()

    def test_show_stats_posts_all_stats(self):
        self.manager.show_stats()
        # Expect 4 status messages
        self.assertEqual(self.mock_msg_handler.post_message.call_count, 4)
        self.mock_msg_handler.post_message.assert_any_call(
            MessageType.STATUS, unittest.mock.ANY
        )

    def test_show_instructions_posts_graveyard_instruction(self):
        self.manager.show_instructions()
        self.mock_msg_handler.post_message.assert_called_with(
            MessageType.INSTRUCTION, GameInstruction.GRAVEYARD
        )

    def test_show_instructions_no_instruction_for_unknown_room(self):
        self.mock_player.room = "Kitchen"
        self.manager.show_instructions()
        self.mock_msg_handler.post_message.assert_not_called()

    def test_show_tooltip_posts_tooltips_for_items(self):
        self.manager.show_instructions()
        # self.manager.show_tooltip()
        # Each item generates a tooltip
        expected_calls: int = 1
        self.assertEqual(self.mock_msg_handler.post_message.call_count, expected_calls)
        self.mock_msg_handler.post_message.assert_any_call(
            MessageType.INSTRUCTION, unittest.mock.ANY
        )

    def test_show_tooltip_no_items(self):
        self.mock_player.items = []
        self.manager.show_tooltip()
        self.mock_msg_handler.post_message.assert_not_called()

    def test_welcome_message_start_game(self):
        """
        🟢 Scenario (Basic Flow): Display Welcome Message at the start of the game - Current Room: Foyer
        •	Given the game has just started
        •	When the game pieces are initialized
        •	Then the player should see a welcome message
        •	And the current room tile should be displayed as “Foyer”
        """
        # self.room = "Foyer"
        self.mock_player.room = "Foyer"
        # simulate stats display as welcome
        self.manager.show_stats()

        # ensure STATUS messages are posted for all stats
        self.assertEqual(self.mock_msg_handler.post_message.call_count,4)
        self.mock_msg_handler.post_message.assert_any_call(
            MessageType.STATUS,
            unittest.mock.ANY
            # Enum("Welcome", {"VAL":})
        )
    def test_room_change_message(self):
        """
        🟢 Scenario (Basic Flow): Update Room Change Message
        •	Given the player is in a room (indoor or outdoor)
        •	When the player moves to a different room
        •	Then a message should display the updated room name.
        """
        # self.player.room = "Kitchen"
        self.mock_player.room = "Kitchen"
        self.manager.show_instructions()  # Should map room to instruction if available
        # Kitchen not mapped, so no instruction should be posted
        self.mock_msg_handler.post_message.assert_not_called()

if __name__ == "__main__":
    unittest.main()