"""
Test suite runner for all item-related tests.

This module loads and runs all item test suites in a single execution,
similar to test_player.py for player tests.

Includes:
    - test_item_helper.py: Tests for get_item() function (target code block)
    - test_oil.py: Tests for Oil item
    - test_gasoline.py: Tests for Gasoline item
    - test_board_with_nails.py: Tests for Board with Nails item
    - test_can_of_soda.py: Tests for Can of Soda item
    - test_grisly_femur.py: Tests for Grisly Femur item
    - test_golf_club.py: Tests for Golf Club item
    - test_candle.py: Tests for Candle item
    - test_chainsaw.py: Tests for Chainsaw item
    - test_machete.py: Tests for Machete item

Usage:
    Run all item tests:
        python -m test.item.test_item_package

    Run with coverage:
        coverage run -m test.item.test_item_package
        coverage html --include="src/model/item/*"
        coverage report

    Run specific to target code block (item_helper.py):
        coverage run -m test.item.test_item_package
        coverage html --include="src/model/item/item_helper.py"
"""
import unittest

# Import target code block test (get_item function)
from .test_item_helper import TestGetItemFunction

# Import individual item tests
from .test_oil import TestOil
from .test_gasoline import TestGasoline
from .test_board_with_nails import TestBoardWithNails
from .test_can_of_soda import TestCanOfSoda
from .test_grisly_femur import TestGrislyFemur
# Note: test_golf_club.py has class TestGrislyFemur (bug in original code)
from .test_golf_club import TestGrislyFemur as TestGolfClubTests
from .test_candle import TestCandle
from .test_chainsaw import TestChainsaw
from .test_machete import TestMachete


def load_item_tests():
    """Load all item test suites into a single test suite.

    This function creates a combined test suite that includes:
    1. Tests for the target code block (get_item function)
    2. Tests for all individual item classes

    Returns:
        unittest.TestSuite: Combined test suite with all item tests
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add target code block test (get_item function) - PRIORITY
    suite.addTests(loader.loadTestsFromTestCase(TestGetItemFunction))

    # Add individual item class tests
    suite.addTests(loader.loadTestsFromTestCase(TestOil))
    suite.addTests(loader.loadTestsFromTestCase(TestGasoline))
    suite.addTests(loader.loadTestsFromTestCase(TestBoardWithNails))
    suite.addTests(loader.loadTestsFromTestCase(TestCanOfSoda))
    suite.addTests(loader.loadTestsFromTestCase(TestGrislyFemur))
    suite.addTests(loader.loadTestsFromTestCase(TestGolfClubTests))
    suite.addTests(loader.loadTestsFromTestCase(TestCandle))
    suite.addTests(loader.loadTestsFromTestCase(TestChainsaw))
    suite.addTests(loader.loadTestsFromTestCase(TestMachete))

    return suite


if __name__ == '__main__':
    # Run all item tests with verbose output
    print("=" * 70)
    print("RUNNING ALL ITEM TESTS")
    print("=" * 70)
    print("\nThis includes:")
    print("  1. Target Code Block: test_item_helper.py (get_item function)")
    print("  2. Individual Items: Oil, Gasoline, Weapons, etc.")
    print("\n" + "=" * 70 + "\n")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(load_item_tests())

    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")

    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED!")
    else:
        print("\n❌ SOME TESTS FAILED")

    print("=" * 70)
