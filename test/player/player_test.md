# Player Model Testing Plan


## Running Tests

### Run All Unit Tests
```bash
# Activate virtual environment
. venv/Scripts/activate

# Run all player tests
python -m pytest test/player/ -v
```

### Run Individual Test Suites
```bash
# Run specific user story tests
python -m pytest test/player/test_player_state.py -v
python -m pytest test/player/test_inventory_management.py -v
python -m pytest test/player/test_item_usage.py -v
python -m pytest test/player/test_item_combination.py -v
```

## Generate Coverage Reports

### Coverage for All Player Tests
```bash
# Run all tests with coverage
python -m pytest test/player/ --cov=src.model.player --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```