# Player Unit Tests

This document explains how to run the unit tests for the Player module and generate coverage reports.

## Test File
- **Location**: `test/player/test_player.py`
- **Test Classes**: 
  - `TestPlayer` - Tests the Player facade class
  - `Test_PlayerImplementation` - Tests the _PlayerImplementation class
- **Total Tests**: 41 test cases

## Running Tests

### Basic Test Execution
```bash
# Run all player tests
python -m pytest test/player/test_player.py -v

# Run from project root directory
cd C:\Users\rishe\Documents\GitHub\ZombieInMyPocket
python -m pytest test/player/test_player.py -v
```

### Run Specific Test Classes
```bash
# Run only TestPlayer class
python -m pytest test/player/test_player.py::TestPlayer -v

# Run only Test_PlayerImplementation class
python -m pytest test/player/test_player.py::Test_PlayerImplementation -v
```

### Run Individual Tests
```bash
# Run specific test method
python -m pytest test/player/test_player.py::TestPlayer::test_init_default_values -v
```

## Coverage Reports

### Generate Coverage with Tests
```bash
# Run tests with coverage collection
python -m coverage run -m pytest test/player/test_player.py -v
```

### View Coverage Report (Terminal)
```bash
# Show coverage report for player module only
python -m coverage report --include="src/model/player/player.py"

# Show detailed report with missing lines
python -m coverage report --include="src/model/player/player.py" --show-missing
```

### Generate HTML Coverage Report
```bash
# Generate interactive HTML report
python -m coverage html --include="src/model/player/player.py" --directory=coverage_report

# Open the report in your browser
# File location: coverage_report/index.html
```
