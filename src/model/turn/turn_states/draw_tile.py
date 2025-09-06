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
        the_new_tile = self.use_service(
            #todo check indoor/outdoor in service
            ServiceNames.GAME_PIECES,
            ServiceMethods.DRAW_TILE,
        )
        self.result = (the_new_tile, Triggers.NEW_TILE_EXIT, *self.args)
        super().handle_request()

    def exit(self):
        super().exit()

