import unittest

# Import all user story test suites
from .test_player_position_tracking import TestPlayerPositionTracking
from .test_player_inventory_limit import TestPlayerInventoryLimit
from .test_combining_items import TestCombiningItems
from .test_health_property import TestHealthProperty
from .test_attack_property import TestAttackProperty
from .test_using_items import TestUsingItems
from .test_dropping_items import TestDroppingItems
from .test_attack_power_calculation import TestAttackPowerCalculation
from .test_totem_tracking import TestTotemTracking
from .test_player_implementation import Test_PlayerImplementation, TestPlayer


def load_user_story_tests():
    """Load all user story test suites into a single test suite.

    This function creates a combined test suite that includes all user story
    tests from their separate files, allowing them to be run as part of the
    main TestPlayer execution.
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all user story test classes
    suite.addTests(loader.loadTestsFromTestCase(TestPlayerPositionTracking))
    suite.addTests(loader.loadTestsFromTestCase(TestPlayerInventoryLimit))
    suite.addTests(loader.loadTestsFromTestCase(TestCombiningItems))
    suite.addTests(loader.loadTestsFromTestCase(TestHealthProperty))
    suite.addTests(loader.loadTestsFromTestCase(TestAttackProperty))
    suite.addTests(loader.loadTestsFromTestCase(TestUsingItems))
    suite.addTests(loader.loadTestsFromTestCase(TestDroppingItems))
    suite.addTests(loader.loadTestsFromTestCase(TestAttackPowerCalculation))
    suite.addTests(loader.loadTestsFromTestCase(TestTotemTracking))
    suite.addTests(loader.loadTestsFromTestCase(Test_PlayerImplementation))
    suite.addTests(loader.loadTestsFromTestCase(TestPlayer))

    return suite


if __name__ == '__main__':
    # Run all tests: user story tests and implementation tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_user_story_tests())
