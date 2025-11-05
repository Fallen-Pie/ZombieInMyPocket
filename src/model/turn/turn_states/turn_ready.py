"""Ready to start a turn"""
from typing import Any
from ..state import State, StateNames, Triggers

#if TYPE_CHECKING:



class Ready(State):
    """Ready to start a turn"""
    def __init__(self, name = StateNames.READY):
        super().__init__(name)
        self.trigger = Triggers.START_TURN


    def enter(self):
        """Ready to start a turn"""
        #no set up needed
        pass


    def handle_request(self):
        """Wait before starting a new turn"""
        #print(f'{'-'*10}starting a new turn{'-'*10}')
        super().handle_request()


    def exit(self):
        super().exit()
        #Expected next state Get player tile

    def get_input_options(self) -> Any:
        """Ready state doesn't need input options"""
        return []

    def get_prompt(self) -> str:
        """Ready state doesn't need a prompt"""
        return "Press Enter to start a new turn..."