# Item Unit Tests

## Testing Strategy

The test suite follows a user story-driven approach. 
Tests are organized by user stories with clear acceptance criteria, ensuring all item mechanics are properly validated. 
The suite includes 21 tests across 4 separate test files covering 3 user stories and implementation level tests.

## Test Structure
- **Main Test Runner**: `test/item/test_item.py` (imports and runs all tests)
- **User Story Files**: Individual test files for each user story (3 files)
- **Implementation Tests**: `test/item/test_item_implementation.py` (detailed class coverage)
- **Total Tests**: 21 test cases across 4 separate test files

## Running Tests

### Run All Unit Tests
```bash
# Activate virtual environment
. venv/Scripts/activate

# Run all item tests
python -m pytest test/item/test_item.py -v

# Run all tests in item directory
python -m pytest test/item/ -v
```

### Run Individual Test Suites
```bash
# Run specific user story tests
python -m pytest test/item/test_single_use_items.py -v
python -m pytest test/item/test_multi_use_items.py -v
python -m pytest test/item/test_refilling_items_by_combination.py -v

# Run implementation tests
python -m pytest test/item/test_item_implementation.py -v
```

## Generate Coverage Reports

### Coverage for All Item Tests
```bash
# Run all tests with coverage
python -m pytest test/item/ --cov=src.model.item --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```

### Coverage for Individual Test Suites
```bash
# Run specific test suite with coverage
python -m pytest test/item/test_base_item.py --cov=src.model.item --cov-report=html

# Run user story test with coverage
python -m pytest test/item/test_single_use_items.py --cov=src.model.item --cov-report=html
```