from src.model.interfaces import IEncounter, IPlayer

class ItemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self, new_item):
        self.item = new_item

    def handle_encounter(self, player) -> IPlayer:
        if player is not IPlayer:
            raise TypeError("Health Encounter can only be handled by a Player")
        player.add_item_to_inventory(self.item)
        return player
