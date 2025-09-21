
from src.model.interfaces.i_player import IPlayer
from src.model.interfaces.i_item import IItem
from src.enums_and_types.types import Position
from src.model.item.base_item import ConsumableItem
from src.model.item.combination_engine import CombinationEngine

class Player(IPlayer):
    """Player iteration-two implementation."""

    def __init__(self, initial_health: int = 6, attack_power: int = 1, inventory_limit: int = 2):
        self._health = initial_health
        self._max_health = initial_health
        self._attack_power = attack_power
        self._inventory: list[IItem] = []
        self._position: Position = (0, 0)
        self._has_totem = False
        self._inventory_limit = inventory_limit
        self._combination_engine = CombinationEngine()

    def get_health(self) -> int:
        """Get the player's current health points."""
        return self._health

    def take_damage(self, amount: int) -> None:
        """Reduce the player's health by the specified amount."""
        # End game logic here?
        if amount < 0:
            return
        self._health -= amount
        if self._health < 0:
            self._health = 0

    def heal(self, amount: int) -> None:
        """Increase the players health by the specified amount."""
        if amount < 0:
            return
        self._health += amount
        if self._health > self._max_health:
            self._health = self._max_health

    def get_attack_power(self) -> int:
        """Get the player's total attack power including item bonuses."""
        bonus = sum(item.attack_bonus for item in self._inventory if hasattr(item, 'attack_bonus'))
        return self._attack_power + bonus

    def has_totem(self) -> bool:
        """Check if the player possesses the evil totem."""
        return self._has_totem

    def get_position(self) -> Position:
        """Get the player's current position on the game board."""
        return self._position

    def set_position(self, position: Position) -> None:
        """Move the player to a new position on the game board."""
        self._position = position

    def use_item(self, item: IItem) -> None:
        """Use an item from the player's inventory."""
        if item in self._inventory:
            if isinstance(item, ConsumableItem):
                self.heal(item.heal_amount)
            
            should_discard = item.use()
            if should_discard:
                self.remove_item_from_inventory(item)

    def get_inventory(self) -> list[IItem]:
        """Get a copy of the player's current inventory."""
        return self._inventory.copy()

    def add_item_to_inventory(self, item: IItem) -> None:
        """Add an item to the player's inventory if there is space."""
        if len(self._inventory) < self._inventory_limit:
            self._inventory.append(item)
        else:
            print("Inventory is full!")

    def remove_item_from_inventory(self, item: IItem) -> None:
        """Remove an item from the player's inventory."""
        if item in self._inventory:
            self._inventory.remove(item)

    def combine_items_from_inventory(self) -> bool:
        """Attempt to combine compatible items in the inventory."""
        # combine should also return combined item to add to inventory
        if len(self._inventory) < 2:
            return False

        for i in range(len(self._inventory)):
            for j in range(i + 1, len(self._inventory)):
                item1 = self._inventory[i]
                item2 = self._inventory[j]

                try:
                    result = self._combination_engine.combine(item1, item2)
                    if result:
                        for item in result.items_consumed:
                            self.remove_item_from_inventory(item)
                        return True
                except ValueError:
                    continue
        return False

    def set_has_totem(self, has_totem: bool) -> None:
        """Set the player's totem status."""
        self._has_totem = has_totem