from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class GetTileEncounter(State):
    def __init__(self, name=StateNames.GET_TILE_ENCOUNTER):
        super().__init__(name)
        self.tile = None

    def enter(self, the_tile, *args):
        self.trigger = Triggers.RUN_ENCOUNTER
        if the_tile is not None:
            self.tile = the_tile

    @staticmethod
    def get_tile_encounter(tile):
        return tile.get_encounter()
        # return self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.GET_ENCOUNTER,
        #     tile = tile
        # )


    def handle_request(self, *arg, **kwarg):
        #todo use the get_player_tile state to get the tile the player has moved to
        #replacing holding the active tile in the context
        the_encounter = self.get_tile_encounter(self.tile)
        if the_encounter:
            self.result = (
                self.get_tile_encounter(self.tile),
                Triggers.TILE_ENCOUNTER_END
            )
        else:
            self.result = None
            self.trigger = Triggers.TILE_ENCOUNTER_END
        super().handle_request()


    def exit(self):
        super().exit()