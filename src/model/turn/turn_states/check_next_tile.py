"""Check if the given tile and exit leads to a new tile or an existing tile."""
from typing import Any
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class CheckNextTile(State):
    """Checks if the next tile on the board is new,
    if it's new a tile needs to be drawn and then placed
    if it's not the player needs to be moved"""
    def __init__(self, name = StateNames.CHECK_NEXT_TILE):
        super().__init__(name)
        self.tile = None
        self.selected_door = None


    def enter(self, a_tile, selected_door):
        self.tile = a_tile
        self.selected_door = selected_door


    def _is_next_tile_new(self, a_tile, selected_door) -> bool:
        """Check if the tile attached to the give door on the give tile is new or not."""
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.IS_NEXT_TILE_NEW,
            a_tile,
            selected_door)


    def _get_next_tile(self) -> Any:
        """Get the next tile"""
        return self.tile #Don't move the player for now
        # return self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.GET_NEXT_TILE,
        #     self.tile,
        #     self.selected_door
        # )

    def handle_request(self, *args, **kwargs) -> None:
        """Check if the next tile is new, set result and trigger accordingly"""
        if self._is_next_tile_new(self.tile, self.selected_door):
            self.result = (self.tile, self.selected_door)
            self.trigger = Triggers.DRAW_TILE
        else:
            #Need to get the next tile to move the player onto
            self.result = (self._get_next_tile(),)
            self.trigger = Triggers.MOVE_PLAYER
        super().handle_request()

    def exit(self) -> None:
        super().exit()
