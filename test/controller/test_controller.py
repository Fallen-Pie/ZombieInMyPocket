import unittest

from test.controller.test_game_controller_initialization import TestGameControllerInitialization
from test.controller.test_game_flow import TestGameFlow
from test.controller.test_game_display import TestGameDisplay
from test.controller.test_game_input import TestGameInput

def load_controller_tests():
    """Load all controller tests into single test suite."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestGameControllerInitialization))
    suite.addTests(loader.loadTestsFromTestCase(TestGameFlow))
    suite.addTests(loader.loadTestsFromTestCase(TestGameDisplay))
    suite.addTests(loader.loadTestsFromTestCase(TestGameInput))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_controller_tests())
