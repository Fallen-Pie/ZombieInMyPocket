from ..state import State
from ..turn_enums import StateNames, ServiceNames, Triggers

class RunEncounter(State):
    """Runs the encounter from the previous state"""
    def __init__(self, name: StateNames = StateNames.RUN_ENCOUNTER):
        super().__init__(name)
        self._encounter = None

    def enter(self, encounter, exit_mode):
        self.trigger = exit_mode
        self._encounter = encounter


    def handle_request(self):
        self._encounter.handle_encounter(
            self.context._get_service(ServiceNames.PLAYER)
        )
        self.result = self.get_result()
        super().handle_request()

    def get_result(self) -> Triggers | None:
        out_put = None
        if self.trigger == Triggers.DEV_ENCOUNTER_END:
            #the next encounter will be a tile so need to get the tile
            out_put = (Triggers.START_TILE_ENCOUNTER, )
        return out_put

    def exit(self):
        super().exit()