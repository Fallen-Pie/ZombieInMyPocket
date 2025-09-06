"""Places a tile"""
from ..state import State
from ..turn_enums import StateNames, ServiceNames, ServiceMethods, Triggers


class PlaceTile(State):
    def __init__(self, name: StateNames = StateNames.PLACE_TILE):
        super().__init__(name)
        self.new_tile = None
        self.new_exit = None
        self.current_tile = None
        self.current_exit = None


    def enter(self, new_tile, new_exit, current_tile, current_exit):
        self.new_tile = new_tile
        self.new_exit = new_exit
        self.current_tile = current_tile
        self.current_exit = current_exit


    def _place_tile(self):
        self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.PLACE_TILE,
            self.new_tile,
            self.new_exit,
            self.current_tile,
            self.current_exit
        )


    def _can_place_tile(self):
        #temp
        # return True #override whilst CAN_PLACE_TILE isn't working
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.CAN_PLACE_TILE,
            self.new_tile,
            self.new_exit,
            self.current_tile,
            self.current_exit
        )

    def handle_request(self, *arg, **kwarg):
        if self._can_place_tile():
            self.trigger = Triggers.MOVE_PLAYER
            self._place_tile()
            self.result = (self.new_tile, )
        else:
            #go back to select exit state
            self.trigger = Triggers.SELECT_EXIT
            self.result = (
                self.new_tile,
                Triggers.NEW_TILE_EXIT,
                self.current_tile,
                self.current_exit
            )
            #This could become an end less loop....

        super().handle_request()


    def exit(self):
        super().exit()