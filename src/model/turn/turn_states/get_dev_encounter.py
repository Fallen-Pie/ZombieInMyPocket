"""Draw a dev card then get the encounter from it based on time"""
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class GetDevEncounter(State):
    def __init__(self, name=StateNames.GET_DEV_ENCOUNTER):
        super().__init__(name)
    
    def enter(self):
        self.trigger = Triggers.RUN_ENCOUNTER

    
    def _get_dev_card(self):
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.DRAW_DEV_CARD
        )

    @staticmethod
    def _get_dev_encounter(dev_card):
        dev_card.get_encounter(9) #todo use game time
        # return self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.GET_ENCOUNTER,
        #     dev_card=dev_card
        # )
    
    def handle_request(self):
        the_dev_card = self._get_dev_card()
        self.result = (
            self._get_dev_encounter(the_dev_card),
            Triggers.DEV_ENCOUNTER_END
        )
        super().handle_request()


    def exit(self):
        super().exit()
    
    