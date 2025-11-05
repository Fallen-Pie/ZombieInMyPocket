from src.common import InputOptions

from src.model.encounters import CowerEncounter

from ..state import State, StateNames, Triggers

class GetCowerEncounter(State):
    def __init__(self, name=StateNames.GET_COWER_ENCOUNTER):
        super().__init__(name)

    def enter(self):
        self.trigger = Triggers.RUN_ENCOUNTER
        self.needs_input = True

    @staticmethod
    def _get_cower_encounter():
        return CowerEncounter()

    @staticmethod
    def get_input_options():
        return [InputOptions.YES, InputOptions.NO]

    @staticmethod
    def get_prompt():
        return "Would you like to cower"

    def handle_request(self, selected_option):
        if selected_option == InputOptions.YES.value:
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
