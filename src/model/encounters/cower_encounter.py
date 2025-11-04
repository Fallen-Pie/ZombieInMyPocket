from src.common import IEncounter, IPlayer

class CowerEncounter(IEncounter):
    """Handles Cower Encounter"""
    HEALTH_INCREASE = 3

    def __init__(self):
        self.health_increase = self.HEALTH_INCREASE

    def handle_encounter(self, player) -> IPlayer:
        if player is not IPlayer:
            raise TypeError("Health Encounter can only be handled by a Player")
        player.heal(self.health_increase)
        return player
