# Modified by David Watts to prevent errors in testing

from abc import ABC, abstractmethod
from ..interfaces.i_player import IPlayer

class IEncounter(ABC):
    """Abstract Class for building other Encounter Classes"""
    @abstractmethod
    def handle_encounter(self, player) -> IPlayer:
        ...

class HealthEncounter(IEncounter):
    """Handles Health Encounters"""
    def __init__(self, value):
        self.health = value

    def handle_encounter(self, player) -> IPlayer:
        player.heal(self.health)
        return player

class CowerEncounter(IEncounter):
    """Handles Cower Encounter"""
    def __init__(self):
        self.health_increase = 3

    def handle_encounter(self, player) -> IPlayer:
        player.heal(self.health_increase)
        return player

class CombatEncounter(IEncounter):
    """Handles Combat Encounters"""
    def __init__(self, value):
        self.zombies = value

    def handle_encounter(self, player) -> IPlayer:
        damage = self.zombies - player.attack_power
        if damage > 4:
            damage = 4
        elif damage < 0:
            damage = 0
        player.take_damage(damage)
        return player
        
class ItemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self, new_item):
        self.item = new_item

    def handle_encounter(self, player) -> IPlayer:
        player.add_item_to_inventory(self.item)
        return player

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
