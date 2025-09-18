import pytest
from src.model.game_session_manager import GameSessionManager
from src.enums_and_types.enums import GameState

@pytest.fixture
def manager():
    return GameSessionManager()

def test_initial_state(manager):
    assert manager.get_current_state() == GameState.INIT
    assert manager.health == 6
    assert manager.attack == 1
    assert manager.room == "Foyer"

def test_set_current_state(manager):
    manager.set_current_state(GameState.PAUSED)
    assert manager.get_current_state() == GameState.PAUSED

def test_set_invalid_state(manager):
    with pytest.raises(ValueError):
        manager.set_current_state("NotAState")

def test_reset_game(manager):
    manager.health = 3
    manager.attack = 5
    manager.room = "Dungeon"
    manager.set_current_state(GameState.RUNNING)

    manager.reset_game()

    assert manager.health == 6
    assert manager.attack == 1
    assert manager.room == "Foyer"
    assert manager.get_current_state() == GameState.INIT