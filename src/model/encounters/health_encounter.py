from src.model.interfaces import IEncounter, IPlayer

class HealthEncounter(IEncounter):
    """Handles Health Encounters"""
    def __init__(self, value):
        self.health = value

    def handle_encounter(self, player) -> IPlayer:
        player.heal(self.health)
        return player
