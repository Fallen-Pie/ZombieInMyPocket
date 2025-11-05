import unittest
from src.model.game_time import GameTime

class MidnightGameOver(unittest.TestCase):
    """
    Midnight loss condition is enforced
    • Given the time reaches midnight
    • When checking the game status
    • Then the game ends and the player loses
    """
    def setUp(self):
        self.game_time = GameTime()

    def test_time_condition_true(self):
        self.game_time.increase_current_time()
        self.game_time.increase_current_time()
        expected_state = self.game_time.is_time_valid()
        self.assertEqual(expected_state, True)

    def test_time_condition_false(self):
        self.game_time.increase_current_time()
        self.game_time.increase_current_time()
        self.game_time.increase_current_time()
        expected_state = self.game_time.is_time_valid()
        self.assertEqual(expected_state, False)

if __name__ == '__main__':
    unittest.main()