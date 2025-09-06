from typing import Any
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods
from src.enums_and_types import Direction

class SelectExit(State):
    """Ask the user to select an exit from a give tile"""
    def __init__(self, name = StateNames.SELECT_EXIT):
        super().__init__(name)
        #self.tile_exits = []
        #self.args = None
        self._tile = None
        self._other_tile = None
        self._other_exit = None


    def enter(
            self,
            the_tile: Any,
            exit_mode: Triggers,
            other_tile = None,
            other_exit = None
    ):

        self._tile = the_tile
        self.trigger = exit_mode

        self._other_tile = other_tile
        self._other_exit = other_exit

        self.needs_input = True

        self.get_user_selection()


    def get_tile_exits (self):
        return self._tile.get_exits()
        # self.tile_exits = self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.GET_TILE_EXITS,
        #     self.result)


    def get_user_selection(self):
        tile_exits = self.get_tile_exits()
        tile_name = self._tile.get_name(),
        self.use_service(
            ServiceNames.UI,
            ServiceMethods.GET_INPUT,
            prompt = f"Pick an exit on the {tile_name} tile",
            options = tile_exits,
            callback = self.get_request_handler())


    def handle_request(self, selected_exit):
        selected_exit = Direction(int(selected_exit))

        if self.trigger == Triggers.NEW_TILE_EXIT:
            #selected an exit on a tile that is about to be placed
            self.result = (
                self._tile,
                selected_exit,
                self._other_tile,
                self._other_exit
            )
            #expected next state PLACE_TILE
        else:
            #selected an exit on a tile that the player is on
            self.result = (
                self._tile,
                selected_exit
            )
            #expected next state CHECK_NEXT_TILE
        self.exit()


    def exit(self):
        super().exit()
        # Expected next state check_new_tile or place_tile