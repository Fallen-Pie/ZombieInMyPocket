from enum import Enum

class StateNames(Enum):
    READY = "ready"
    GET_PLAYER_TILE = "get_player_tile"
    SELECT_EXIT = "select_exit"
    CHECK_NEXT_TILE = "check_next_tile"
    DRAW_TILE = "draw_tile"
    PLACE_TILE = "place_tile"
    MOVE_PLAYER = "move_player"
    GET_DEV_ENCOUNTER = "get_dev_encounter"
    GET_TILE_ENCOUNTER = "get_tile_encounter"
    GET_COWER_ENCOUNTER = "get_cower_encounter"
    RUN_ENCOUNTER = "run_encounter"