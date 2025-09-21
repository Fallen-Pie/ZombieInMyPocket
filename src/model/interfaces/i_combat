from abc import ABC, abstractmethod

class ICombat(ABC):
    @abstractmethod
    def start_combat(self, player):
        """Start the combat phase for the given player."""
        pass

    @abstractmethod
    def calculate_damage(self, player, num_zombies, player_attack):
        """Calculate and return damage based on player and zombie stats."""
        pass

    @abstractmethod
    def handle_cower(self, player):
        """Handle the player choosing to cower in combat."""
        pass

    @abstractmethod
    def handle_runaway(self, player, RUN_AWAY_DAMAGE):
        """Handle the player choosing to run away from combat."""
        pass

    @abstractmethod
    def get_combat_options(self):
        """Return a list of combat options available to the player."""
        pass
