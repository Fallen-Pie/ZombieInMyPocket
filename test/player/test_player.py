import unittest
from test.player.test_inventory_management import TestInventoryManagement
from test.player.test_item_combination import TestItemCombination
from test.player.test_item_usage import TestItemUsage
from test.player.test_player_state import TestPlayerState




def build_suite():
    """Build the test suite."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestInventoryManagement))
    suite.addTests(loader.loadTestsFromTestCase(TestItemCombination))
    suite.addTests(loader.loadTestsFromTestCase(TestItemUsage))
    suite.addTests(loader.loadTestsFromTestCase(TestPlayerState))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(build_suite())