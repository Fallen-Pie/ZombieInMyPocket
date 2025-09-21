from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class MovePlayer(State):
    """Moves the player
    expected previous state:
         check_new_tile
         place_tile
    """
    def __init__(self, name=StateNames.MOVE_PLAYER):
        super().__init__(name)
        self.the_tile = None
        #self.selected_exit = None


    def enter(
            self,
            a_tile,
            #selected_exit
    ):
        self.trigger = Triggers.START_ENCOUNTERS
        self.the_tile = a_tile
        #self.the_tile = a_tile
        #self.selected_exit = selected_exit



    def _get_tile_position(self, a_tile):
        #return 1, 0
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.GET_TILE_POSITION,
            a_tile
        )
        #error with get_tile_position


    def _move_player(self, position):
        self.use_service(
            ServiceNames.PLAYER,
            ServiceMethods.SET_POSITION,
            position
        )


    def handle_request(self, *arg, **kwarg):
        self._move_player(self._get_tile_position(self.the_tile))
        super().handle_request()


    def exit(self):
        super().exit()
