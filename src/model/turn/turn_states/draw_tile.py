from typing import Any
from ..state import State
from ..turn_enums import ServiceNames, ServiceMethods, Triggers, StateNames

#from src.enums_and_types.types import Position

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
        self.result = self.use_service(
            #todo check indoor/outdoor in service
            ServiceNames.GAME_PIECES,
            ServiceMethods.DRAW_TILE,
        )
        super().handle_request()

    def exit(self):
        self.result = (self.result, Triggers.NEW_TILE_EXIT, *self.args)
        super().exit()

    def get_input_options(self) -> Any:
        """No input options needed for drawing tile"""
        return []

    def get_prompt(self) -> str:
        """No prompt needed for drawing tile"""
        return "Drawing a new tile..."
