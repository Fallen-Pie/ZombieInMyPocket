"""Player implementation for the Zombie in My Pocket game.

This module contains the Player class and its implementation that handles
all player functionality including health, combat, inventory management,
movement, and item interactions including combinations.
"""

from ..interfaces.i_player import IPlayer
from ..interfaces.i_item import IItem
from ..item.item_helper import combine_items
from src.enums_and_types.types import Position


class Player(IPlayer):
    """Player wrapper class that implements the IPlayer interface.
    
    This class serves as a facade for the internal _PlayerImplementation,
    providing a clean interface that matches the IPlayer contract while
    delegating actual functionality to the implementation class.
    """
    def __init__(self, initial_health: int = 100,
                 initial_position: Position = (0, 0),
                 base_attack_power: int = 1):
        """Initialize a new player.
        
        Args:
            initial_health: Starting health points (default: 100)
            initial_position: Starting position on the board (default: (0, 0))
            base_attack_power: Base attack value (default: 1)
        """
        self.__player_impl = _PlayerImplementation(
            initial_health, initial_position, base_attack_power)

    def get_health(self) -> int:
        """Get the player's current health points.
        
        Returns:
            Current health as an integer
        """
        return self.__player_impl.health

    def get_attack_power(self) -> int:
        """Get the player's total attack power including item bonuses.
        
        Returns:
            Total attack value including base stats and equipped item bonuses
        """
        return self.__player_impl.attack_power

    def get_position(self) -> Position:
        """Get the player's current position on the game board.
        
        Returns:
            The player's current Position coordinates
        """
        return self.__player_impl.position

    def set_position(self, position: Position) -> None:
        """Move the player to a new position on the game board.
        
        Args:
            position: The new Position coordinates for the player
        """
        self.__player_impl.position = position

    def get_inventory(self) -> list[IItem]:
        """Get a copy of the player's current inventory.
        
        Returns:
            List of items currently in the player's possession
        """
        return self.__player_impl.inventory

    def take_damage(self, amount: int) -> None:
        """Reduce the player's health by the specified amount.
        
        Args:
            amount: Number of health points to remove
        """
        self.__player_impl.take_damage(amount)

    def heal(self, amount: int) -> None:
        """Increase the player's health by the specified amount.
        
        Args:
            amount: Number of health points to restore
        """
        self.__player_impl.heal(amount)

    def has_totem(self) -> bool:
        """Check if the player possesses the evil totem.
        
        Returns:
            True if the player has the totem, False otherwise
        """
        return self.__player_impl.has_totem

    def use_item(self, item: IItem) -> None:
        """Use an item from the player's inventory.
        
        Args:
            item: The item to use from inventory
        """
        self.__player_impl.use_item(item)

    def add_item_to_inventory(self, item: IItem) -> None:
        """Add an item to the player's inventory.
        
        Args:
            item: The item to add to inventory
        """
        self.__player_impl.add_item_to_inventory(item)

    def remove_item_from_inventory(self, item: IItem) -> None:
        """Remove an item from the player's inventory.
        
        Args:
            item: The item to remove from inventory
        """
        self.__player_impl.remove_item_from_inventory(item)

    def combine_items_from_inventory(self) -> bool:
        """Attempt to combine compatible items in the inventory.
        
        Returns:
            True if a combination was successful, False otherwise
        """
        return self.__player_impl.combine_items_from_inventory()


class _PlayerImplementation:
    """Concrete implementation of player functionality.
    
    This class contains the actual implementation of all player mechanics
    including health management, inventory handling, combat calculations,
    and item usage. It maintains the player's state and provides methods
    for modifying that state.
    """

    def __init__(self, initial_health: int, initial_position: Position,
                 base_attack_power: int):
        """Initialize the player implementation with starting values.
        
        Args:
            initial_health: Starting health points
            initial_position: Starting position coordinates on the board
            base_attack_power: Base attack value without item bonuses
        """
        self._health = initial_health
        self._base_attack_power = base_attack_power
        self._inventory: list[IItem] = []
        self._position = initial_position
        self._has_totem = False

    @property
    def health(self) -> int:
        """Get the current health points.
        
        Returns:
            Current health value
        """
        return self._health

    @property
    def attack_power(self) -> int:
        """Get the total attack power including item bonuses.
        
        Currently returns only base attack power. Item bonuses are
        calculated during combat through use_item method.
        
        Returns:
            Base attack power value
        """
        return self._base_attack_power

    @property
    def has_totem(self) -> bool:
        """Check if the player possesses the evil totem.
        
        Returns:
            True if player has the totem, False otherwise
        """
        return self._has_totem

    @property
    def inventory(self) -> list[IItem]:
        """Get a copy of the current inventory.
        
        Returns:
            Copy of the inventory list to prevent external modification
        """
        return self._inventory.copy()

    @property
    def position(self) -> Position:
        """Get the current board position.
        
        Returns:
            Current position coordinates as a tuple
        """
        return self._position

    @position.setter
    def position(self, position: Position) -> None:
        """Set a new board position.
        
        Args:
            position: New position coordinates as a tuple
        """
        self._position = position

    def take_damage(self, amount: int) -> None:
        """Reduce health by the specified amount.
        
        Health cannot go below 0.
        
        Args:
            amount: Number of health points to remove
        """
        self._health = max(0, self._health - amount)

    def heal(self, amount: int) -> None:
        """Increase health by the specified amount.
        
        Args:
            amount: Number of health points to restore
        """
        self._health += amount

    def use_item(self, item: IItem) -> None | int:
        """Use an item from the inventory.
        
        Applies the item's effects: healing items restore health,
        weapon items return attack bonus. Items with 0 uses remaining
        are automatically removed from inventory.
        
        Args:
            item: The item to use from inventory
            
        Returns:
            Attack bonus if using a weapon, None for other items
        """
        if item in self._inventory:
            if item.type.value == 1:
                self.heal(item.heal_amount)
            elif item.type.value == 0:
                return self.attack_power + item.attack_bonus

            if item.uses_remaining == 0:
                self._inventory.remove(item)

    def add_item_to_inventory(self, item: IItem) -> None:
        """Add an item to the inventory if space is available.
        
        Inventory is limited to 2 items maximum.
        
        Args:
            item: The item to add to inventory
        """
        if len(self._inventory) < 2:
            self._inventory.append(item)

    def remove_item_from_inventory(self, item: IItem) -> None:
        """Remove a specific item from the inventory.
        
        Args:
            item: The item to remove from inventory
        """
        if item in self._inventory:
            self._inventory.remove(item)

    def combine_items_from_inventory(self):
        """Attempt to combine the two items in inventory.
        
        Only works if inventory contains exactly 2 items that can
        be combined according to game rules. Used items are automatically
        removed from inventory.
        
        Returns:
            True if combination kills all zombies, False otherwise
        """
        if len(self._inventory) == 2:
            item_a, item_b = self._inventory[0], self._inventory[1]
            try:
                kill_all_zombies = combine_items(item_a, item_b)

                # Remove items with 0 uses_remaining
                items_to_remove: list[IItem] = []
                if item_a.uses_remaining == 0:
                    items_to_remove.append(item_a)
                if item_b.uses_remaining == 0:
                    items_to_remove.append(item_b)

                for item in items_to_remove:
                    self._inventory.remove(item)

                return kill_all_zombies
            except AssertionError:
                return False

        return False
