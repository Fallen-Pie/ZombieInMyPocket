from src.model.interfaces import IEncounter, IPlayer

class ItemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self, new_item):
        self.item = new_item

    def handle_encounter(self, player) -> IPlayer:
        player.add_item_to_inventory(self.item)
        return player
