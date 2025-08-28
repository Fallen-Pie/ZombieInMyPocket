"""Get the players tile"""
from typing import Any
from ..state import State
from ..turn_enums import StateNames, ServiceNames, ServiceMethods, Triggers


class GetPlayerTile(State):
    def __init__(self, name: StateNames = StateNames.GET_PLAYER_TILE):
        super().__init__(name)
        self.player_location = None

    def enter(self, *args) -> None:
        self.trigger = Triggers.SELECT_EXIT


    def get_player_location(self) -> None:
        """Gets the players location"""
        self.player_location = self.use_service(
            ServiceNames.PLAYER,
            ServiceMethods.GET_POSITION)


    def get_player_tile(self):
        """Gets the players tile"""
        self.result = self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.GET_TILE,
            self.player_location)


    def handle_request(self, *args, **kwargs):
        """Get the players location and the tile at that location"""
        self.get_player_location()
        self.get_player_tile()
        super().handle_request()


    def exit(self) -> None:
        a_tile = self.result
        self.result = (a_tile, Triggers.PLAYER_TILE_EXIT)
        self.context.state_finished(
            trigger=self.trigger,
            result=self.result,
            next_tile=a_tile)
        self.context = None
        #Expected next state select_exit

    def get_input_options(self) -> Any:
        """No input options needed for getting player tile"""
        return []

    def get_prompt(self) -> str:
        """No prompt needed for getting player tile"""
        return "Getting current player location..."