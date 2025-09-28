# Controller Unit Tests


## Testing Strategy

For unit testing the controller it be in isolation. To achive this the @patch decorator is used.
This replaces the controller dependencies with mock objects and means we don't have to rely on the actual implementation of these objects.

## Test Structure

-   **Main Test Runner**: `test/controller/test_controller.py` (imports and runs all controller tests)
-   **User Story Files**: Individual test files for each area of functionality:
    -   `test_game_controller_initialization.py`: Covers the initialization of the `GameController`.
    -   `test_game_flow.py`: Covers the game flow management, including starting the game and processing turns.
    -   `test_game_display.py`: Covers the display of game state and messages.
    -   `test_game_input.py`: Covers the handling of user input.

## Running Tests

### Run All Controller Unit Tests

```bash
# Activate virtual environment
. venv/Scripts/activate

# Run all controller tests
python -m unittest test/controller/test_controller.py
```

### Run Individual Test Suites

```bash
# Run specific user story tests
python -m unittest test/controller/test_game_controller_initialization.py
python -m unittest test/controller/test_game_flow.py
python -m unittest test/controller/test_game_display.py
python -m unittest test/controller/test_game_input.py
```

## Generate Coverage Reports

### Coverage for All Controller Tests

```bash
# Run all tests with coverage for the controller
python -m pytest test/controller/ --cov=src.controller --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```
