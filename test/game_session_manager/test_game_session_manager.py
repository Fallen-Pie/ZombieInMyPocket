from unittest.mock import Mock
from src.model.game_session_manager import GameSessionManager
from src.enums_and_types.game_state import GameState

def test_game_over_when_hp_zero():
    player = Mock(hp=0)
    time = Mock(is_midnight=lambda: False)
    turn = Mock(number=1)
    totem = Mock(is_buried=False)
    messenger = Mock()

    session = GameSessionManager(player, time, turn, totem, messenger)

    assert session.is_game_over() is True


def test_game_snapshot_structure():
    player = Mock(hp=5, reset=lambda: None)
    time = Mock(is_midnight=lambda: False, __str__=lambda s: "11:00pm", reset=lambda: None)
    turn = Mock(number=2, reset=lambda: None)
    totem = Mock(is_buried=False, reset=lambda: None)
    messenger = Mock(clear_messages=lambda: None)

    session = GameSessionManager(player, time, turn, totem, messenger)
    snap = session.get_snapshot()

    assert snap["hp"] == 5
    assert snap["time"] == "11:00pm"
    assert snap["turn"] == 2
    assert snap["totem_buried"] is False

# def test_initial_state(manager):
#     assert manager.get_current_state() == GameState.INIT
#     assert manager.health == 6
#     assert manager.attack == 1
#     assert manager.room == "Foyer"
#
# def test_set_current_state(manager):
#     manager.set_current_state(GameState.PAUSED)
#     assert manager.get_current_state() == GameState.PAUSED
#
# def test_set_invalid_state(manager):
#     with pytest.raises(ValueError):
#         manager.set_current_state("NotAState")
#
# def test_reset_game(manager):
#     manager.health = 3
#     manager.attack = 5
#     manager.room = "Dungeon"
#     manager.set_current_state(GameState.RUNNING)
#
#     manager.reset_game()
#
#     assert manager.health == 6
#     assert manager.attack == 1
#     assert manager.room == "Foyer"
#     assert manager.get_current_state() == GameState.INIT