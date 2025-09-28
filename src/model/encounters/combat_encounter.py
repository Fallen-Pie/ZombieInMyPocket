from src.model.interfaces import IEncounter, IPlayer

class CombatEncounter(IEncounter):
    """Handles Combat Encounters"""
    MAX_DAMAGE = 4
    MIN_DAMAGE = 0

    def __init__(self, value):
        self.zombies = value

    def handle_encounter(self, player) -> IPlayer:
        if player is not IPlayer:
            raise TypeError("Health Encounter can only be handled by a Player")
        damage = self.zombies - player.get_attack_power()
        if damage > self.MAX_DAMAGE:
            damage = self.MAX_DAMAGE
        elif damage < self.MIN_DAMAGE:
            damage = self.MIN_DAMAGE
        player.take_damage(damage)
        return player
