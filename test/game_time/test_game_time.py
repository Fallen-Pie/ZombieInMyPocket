import unittest

from src.model.game_time import GameTime


class TestGameTime(unittest.TestCase):
    def setUp(self):
        self.game_time = GameTime()

    def test_game_time_increase(self):
        self.game_time.increase_current_time()
        self.assertEqual(self.game_time.get_current_time(), 10)

    def test_game_time_valid_true(self):
        self.game_time.increase_current_time()
        self.game_time.increase_current_time()
        expected_state = self.game_time.is_time_valid()
        self.assertEqual(expected_state, True)

    def test_game_time_valid_false(self):
        self.game_time.increase_current_time()
        self.game_time.increase_current_time()
        self.game_time.increase_current_time()
        expected_state = self.game_time.is_time_valid()
        self.assertEqual(expected_state, False)

if __name__ == '__main__':
    unittest.main()
