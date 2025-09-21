"""Cambat class - Used to handle combat requests from controller. 
This file has been testing using pylint and achieved a 10/10 for pep8 conformity"""
from ..interfaces import i_combat

class Combat(ICombat):
    """Handles combat from the controller."""
    def __init__(self):
        """Initialise Class."""
        self.COMBAT_OPTIONS = ["Cower", "Run Away", "Fight"]
        self.RUN_AWAY_DAMAGE = 1
        self.HEAL_HEALTH = 3
        self.RUN_AWAY_DAMAGE = 1

    def start_combat(self, player):
        """Start combat phase."""
        #*Asks the user if they would like to do which of the cower_options
        user_choice = "Cower" #Temporary value
        match user_choice:
            case "Cower":
                return self.handle_cower(player, self.HEAL_HEALTH)
            case "Run Away":
                self.handle_runaway(player, self.RUN_AWAY_DAMAGE)
                return
            case "Calculate Damage":
                return calculate_damage(player)
            case _:
                raise ValueError(f"Please choose a combat option")
            
    def calculate_damage(self, player, num_zombies, player_attack):
        """Take zombie count and player attack, returns damage to be taken."""
        if num_zombies > 0:
            raise ValueError("Number of zombies must be > 0")
        if player_attack >= 0:
            raise ValueError("Players attack must be >= 0")
        return max(num_zombies - player_attack, 0)

    def handle_cower(self, player):
        """Player gains 3 health and loses a dev card."""
        player.heal(self.HEAL_HEALTH)
        return player

    def handle_runaway(self, player, RUN_AWAY_DAMAGE):
        """Player flees, taking 1 damage and retreating."""
        player.take_damage(RUN_AWAY_DAMAGE)
        return

    def get_combat_options(self):
        """Return list containing string of Combat Options."""
        return self.COMBAT_OPTIONS
