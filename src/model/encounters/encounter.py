class EncounterContext(object):
    def __init__(self, encounter):
        self.__current_behavior = encounter

    def set_encounter(self, encounter_behaviour):
        self.__current_behavior = encounter_behaviour

    def use_encounter(self, player):
        self.__current_behavior.handle_encounter(player)

