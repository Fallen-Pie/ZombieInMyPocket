"""Ready to start a turn"""
#from typing import TYPE_CHECKING
from ..state import State
from ..turn_enums import StateNames, Triggers

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