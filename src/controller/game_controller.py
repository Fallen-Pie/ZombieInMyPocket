
#from time import sleep
from typing import Any, Callable

from src.common import MessageCode
from src.model import GameStatus, GamePieces, GameTime, Player, Turn
from src.view import DummyUI

class GameController:
    def __init__(self):
        self.game_status = GameStatus()
        self.ui = DummyUI()
        self.game_time = GameTime()
        self.player = Player()
        self.game_pieces = GamePieces(self.game_time)
        self.the_turn = Turn.create(self.game_pieces, self.player, self, self.game_time)

        self.input_callback = None
        self.input_prompt = ""
        self.input_options = ""


    def begin_game(self):
        self.game_status.post_message(MessageCode.WELCOME)
        self.run_game()


    def run_game(self):
        self.the_turn.start_turn()

        while not self.game_status.is_game_over:
            self._process_and_display_messages()
            self._update_full_state()
            
            if self.the_turn.is_waiting_for_callback():
                self.input_callback(self._get_input())
            else:
                 self.the_turn.continue_turn()
            #sleep(0.5)

        self.the_turn.end_turn()

    def get_input_with_callback(self, prompt: str, options: Any,
                              callback: Callable[[Any], None]) -> None:
        """Get input and call the callback with the result."""
        self.input_prompt = prompt
        self.input_options = options
        self.input_callback = callback

    def _get_input(self):
        """Uses the view to get input from the user"""
        return self.ui.get_input(self.input_prompt, self.input_options)


    def _process_and_display_messages(self):
        """Helper to get messages from GameStatus and display them."""
        messages = self.game_status.get_messages()
        if messages:
            for msg in messages:
                self.ui.display_message(msg)
            self.game_status.clear_messages()

    def _update_full_state(self):
        """""Update the game display with current state"""""
        # active_tile = self.game_pieces.get_tile(self.player.get_position())
        #
        # if active_tile:
        #     self.ui.display_game_state(
        #         tile=active_tile,
        #         tile_position=self.game_pieces.get_tile_position(active_tile),
        #     )

        self.ui.display_player_state(
            player_health=self.player.get_health(),
            player_attack=self.player.get_attack_power(),
            items=[item.name for item in self.player.get_inventory()]
        )

        self.ui.display_board(self.game_pieces.get_all_tiles())
