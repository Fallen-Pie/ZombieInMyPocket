from src.common import IEncounter, IPlayer

class HealthEncounter(IEncounter):
    """Handles Health Encounters"""
    def __init__(self, value):
        self.health = value

    def handle_encounter(self, player) -> IPlayer:
        if player is not IPlayer:
            raise TypeError("Health Encounter can only be handled by a Player")
        player.heal(self.health)
        return player
