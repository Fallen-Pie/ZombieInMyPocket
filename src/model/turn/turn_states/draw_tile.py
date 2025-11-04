from typing import Any
from ..state import State, ServiceNames, ServiceMethods, Triggers, StateNames

#from src.common.types import Position

class DrawTile(State):
    """gets a tile, if with position returns the tile at that position,
     if no position draws a new tile indoors or outdoors"""
    def __init__(self, name = StateNames.DRAW_TILE):
        super().__init__(name)
        self.args = None

    def enter(self, *args):
        self.trigger = Triggers.SELECT_EXIT
        self.args = args


    def handle_request(self):
        the_new_tile = self.use_service(
            #todo check indoor/outdoor in service
            ServiceNames.GAME_PIECES,
            ServiceMethods.DRAW_TILE,
        )
        self.result = (the_new_tile, Triggers.NEW_TILE_EXIT, *self.args)
        super().handle_request()

    def exit(self):
        super().exit()

    def get_input_options(self) -> Any:
        """No input options needed for drawing tile"""
        return []

    def get_prompt(self) -> str:
        """No prompt needed for drawing tile"""
        return "Drawing a new tile..."
