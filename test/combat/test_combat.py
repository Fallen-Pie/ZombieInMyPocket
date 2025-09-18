import unittest
from combat import Combat

from src.model.combat import *

class Player:
    def __init__(self):
        self.health = 100
        self.damage_taken = 0

    def heal(self, amount):
        self.health += amount

    def take_damage(self, amount):
        self.health -= amount
        self.damage_taken += amount

    def get_health(self):
        return self.health


class TestCombat(unittest.TestCase):
    def setUp(self): 
        self.combat = Combat()
        self.player = Player()
        
    def test_cower(self):
        self.combat.handle_cower(self.player)  
        self.assertEqual(self.player.get_health(), 103) 
        
    def test_runaway(self):
        self.combat.handle_runaway(self.player)  
        self.assertEqual(self.player.get_health(), 99)

    def test_get_combat_options(self):
        combat_options = self.combat.get_combat_options()
        self.assertIn('Cower', combat_options)
        self.assertIn('Run Away', combat_options)
        self.assertIn('Start Combat', combat_options)
        self.assertIn('Calculate Damage', combat_options)

    def test_calculate_damage_greaterOrEqualtoZero(self):
        self.assertEqual(self.combat.calculate_damage(2,5),0)

    def test_calculate_damage_zombieGreaterThanAttack(self):
        self.assertEqual(self.combat.calculate_damage(5,2),3)
        

if __name__ == "__main__":
    unittest.main()
