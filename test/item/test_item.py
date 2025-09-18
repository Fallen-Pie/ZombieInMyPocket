import unittest

# Import all user story test suites
from .test_single_use_items import TestSingleUseItems
from .test_multi_use_items import TestMultiUseItems
from .test_refilling_items_by_combination import (
    TestRefillingItemsByCombination
)
from .test_item_implementation import (
    TestBaseItem, TestConsumableItem, TestWeaponItem,
    TestCombinableItem, TestSpecialWeaponItem
)


def load_user_story_tests():
    """Load all user story test suites into a single test suite.

    This function creates a combined test suite that includes all user story
    tests from their separate files, allowing them to be run as part of the
    main test execution.
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all user story test classes
    suite.addTests(loader.loadTestsFromTestCase(TestSingleUseItems))
    suite.addTests(loader.loadTestsFromTestCase(TestMultiUseItems))
    suite.addTests(loader.loadTestsFromTestCase(
        TestRefillingItemsByCombination
    ))

    # Add all implementation test classes
    suite.addTests(loader.loadTestsFromTestCase(TestBaseItem))
    suite.addTests(loader.loadTestsFromTestCase(TestConsumableItem))
    suite.addTests(loader.loadTestsFromTestCase(TestWeaponItem))
    suite.addTests(loader.loadTestsFromTestCase(TestCombinableItem))
    suite.addTests(loader.loadTestsFromTestCase(TestSpecialWeaponItem))

    return suite


if __name__ == '__main__':
    # Run all tests: user story tests and implementation tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_user_story_tests())
