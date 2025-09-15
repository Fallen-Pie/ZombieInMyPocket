"""Encounter Class"""

"""Parent Encounter Class"""
class Encounter:
    def __init__(self, value=None):
        self._value = value
        
    @property
    def value(self):
        """Get encounter value"""
        return self._value

    @value.setter
    def value(self, new_value):
        """Set encounter value"""
        self._value = new_value

    def handle_encounter(self, player):
        """Base method to be overridden by child classes"""
        raise NotImplementedError("Subclasses must implement handle_encounter")


"""Child Classess"""
class TotemEncounter(Encounter):
    """Encounter where the player finds a totem"""

    def handle_encounter(self, player):
        player.inventory.append("Totem")
        return player

class HealthEncounter(Encounter):
    """Encounter where the player gains health"""

    def handle_encounter(self, player):
        player.health += 3
        return player

class ItemEncounter(Encounter):
    """Encounter where the player finds an item"""

    def handle_encounter(self, player):
        player.add_item_to_inventory(self.item)
        return player

class MessageEncounter(Encounter):
    """Encounter that gives a message"""

    def handle_encounter(self, player):
        return self.value()


class CombatEncounter(Encounter):
    """Encounter that starts combat"""

    def handle_encounter(self, player):
        combat.start_combat(player)

        

    
