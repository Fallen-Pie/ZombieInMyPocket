import unittest
from unittest.mock import Mock

from src.enums_and_types.direction import Direction
from src.enums_and_types.game_message import MessageType
from src.model.game_pieces.tile import Tile
from src.model.game_time import GameTime
from src.model.player import Player
from src.model.interfaces.i_game_message_getter import IGameMessageGetter
from src.model.game_message_getter.info_message_manager import InfoMessageManager


class TestInfoMessageManager(unittest.TestCase):
    def set_up(self):
        """ Mocking dependencies"""
        self.mock_msg_handler = IGameMessageGetter
        self.player = Player,
        self.tile = Tile,
        self.time = GameTime,

        self.manager = (
            self.mock_msg_handler,
            self.tile,
            self.time,

            # self.player = new Player(self.player),
            # self.player.room = Tile("Foyer",  False, exits=[Direction.NORTH]),
            # self.turn
        )
        self.msg_handler = InfoMessageManager(self.player, self.room, self.mock_msg_handler)

    def test_welcome_message_start_game(self):
        """
        🟢 Scenario (Basic Flow): Display Welcome Message at the start of the game - Current Room: Foyer
        •	Given the game has just started
        •	When the game pieces are initialized
        •	Then the player should see a welcome message
        •	And the current room tile should be displayed as “Foyer”
        """
        self.room = "Foyer"

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
        self.player.room = "Kitchen"
        self.manager.show_instructions()  # Should map room to instruction if available
        # Kitchen not mapped, so no instruction should be posted
        self.mock_msg_handler.post_message.assert_not_called()

if __name__ == "__main__":
    unittest.main()