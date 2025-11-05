# Modified by David Watts to prevent errors in testing

from src.common import IEncounter, IPlayer

class MessageEncounter(IEncounter):
    """Handles Message Encounters"""
    def __init__(self, new_code):
        self.message_code = new_code

    def handle_encounter(self, player) -> IPlayer:
        pass

class TotemEncounter(IEncounter):
    """Handles Totem Encounters"""
    def __init__(self, new_totem_state):
        self.totem_state = new_totem_state

    def handle_encounter(self, player) -> IPlayer:
        # player.setTotem??
        # return player
        pass