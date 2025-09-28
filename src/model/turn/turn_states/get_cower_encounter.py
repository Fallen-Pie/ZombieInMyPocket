import src.model.encounters.cower_encounter
from src.enums_and_types.enums import Input_options
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods
from src.model.encounters import not_implemented_encounters

class GetCowerEncounter(State):
    def __init__(self, name=StateNames.GET_COWER_ENCOUNTER):
        super().__init__(name)

    def enter(self):
        self.trigger = Triggers.RUN_ENCOUNTER
        self.needs_input = True

    @staticmethod
    def _get_cower_encounter():
        return src.model.encounters.cower_encounter.CowerEncounter()

    def get_input_options(self):
        return [Input_options.YES, Input_options.NO]

    def get_prompt(self):
        return "Would you like to cower"

    def handle_request(self, selected_option):
        if selected_option == '0': #Input_options.YES.value:
            print("starting cower encounter")
            self.result = (
                self._get_cower_encounter(),
                Triggers.COWER_ENCOUNTER_END
            )
            self.trigger = Triggers.RUN_ENCOUNTER
        else:
            print("cower encounter skipped")
            self.result = None
            self.trigger = Triggers.COWER_ENCOUNTER_END
        self.exit()

    def exit(self):
        super().exit()
