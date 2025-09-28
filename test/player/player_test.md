# Player Unit Tests

## Testing Strategy

The test suite follows a user story-driven approach. 
Tests are organized by user stories with clear acceptance criteria, ensuring all game mechanics are properly validated. 
The suite includes 64 tests across 10 separate test files covering 9 user stories and additional file for implementation level testing.

## Test Structure
- **Main Test Runner**: `test/player/test_player.py` (imports and runs all tests)
- **User Story Files**: Individual test files for each user story (9 files)
- **Implementation Tests**: `test/player/test_player_implementation.py` (facade and implementation coverage)
- **Total Tests**: 64 test cases across 10 separate test files

## Running Tests

### Run All Unit Tests
```bash
# Activate virtual environment
. venv/Scripts/activate

# Run all player tests
python -m pytest test/player/test_player.py -v

# Run all tests in player directory
python -m pytest test/player/ -v
```

### Run Individual Test Suites
```bash
# Run specific user story tests
python -m pytest test/player/test_combining_items.py -v
python -m pytest test/player/test_totem_tracking.py -v
python -m pytest test/player/test_attack_power_calculation.py -v
python -m pytest test/player/test_player_position_tracking.py -v
python -m pytest test/player/test_player_inventory_limit.py -v
python -m pytest test/player/test_health_property.py -v
python -m pytest test/player/test_attack_property.py -v
python -m pytest test/player/test_using_items.py -v
python -m pytest test/player/test_dropping_items.py -v

# Run implementation tests
python -m pytest test/player/test_player_implementation.py -v
```

## Generate Coverage Reports

### Coverage for All Player Tests
```bash
# Run all tests with coverage
python -m pytest test/player/ --cov=src.model.player --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```

### Coverage for Individual Test Suites
```bash
# Run specific test suite with coverage
python -m pytest test/player/test_player.py --cov=src.model.player --cov-report=html

# Run user story test with coverage
python -m pytest test/player/test_combining_items.py --cov=src.model.player --cov-report=html
```

## Tutor Given Test Cases

The following specific test cases fulfill the tutor's given requirements:

### Weapon Equip Effect
**Given the player equips a weapon, When the player fights zombies, Then the weapon bonus is applied.**
- **Test**: `Test_PlayerImplementation.test_use_item_weapon_type` in `test_player_implementation.py`
- **Coverage**: Verifies weapon items return attack bonus when used (base attack + weapon bonus)
- **Command**: 
```bash
python -m pytest test/player/test_player_implementation.py::Test_PlayerImplementation::test_use_item_weapon_type -v
```

### Combat with Gasoline and Candle  
**Given the player equips Gasoline and Candle, When fighting zombies using Gasoline and Candle, Then all zombies on the tile are killed, And Gasoline is removed from inventory, and player health is unaffected.**
- **Test**: `Test_PlayerImplementation.test_combat_with_gasoline_and_candle` in `test_player_implementation.py`
- **Coverage**: Verifies gasoline is removed (uses_remaining=0), candle remains in inventory, and player health is unaffected
- **Command**: 
```bash
python -m pytest test/player/test_player_implementation.py::Test_PlayerImplementation::test_combat_with_gasoline_and_candle -v
```