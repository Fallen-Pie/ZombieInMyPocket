from enum import Enum

#States and Triggers
class Triggers(Enum):

    START_TURN = "start_turn"

    PLAYER_TILE_EXIT = "player_tile_exit"
    NEW_TILE_EXIT = "new_tile_exit"

    DRAW_TILE = "draw_tile"
    MOVE_PLAYER = "move_player"

    SELECT_EXIT = "select_exit"

    START_ENCOUNTERS = "start_encounters"
    RUN_ENCOUNTER = "run_encounter"
    DEV_ENCOUNTER_END = "dev_encounter_end"
    START_TILE_ENCOUNTER = "start_tile_encounter"
    TILE_ENCOUNTER_END = "tile_encounter_end"
    COWER_ENCOUNTER_END = "cow_encounter_end"

    NEXT_TURN = "next_turn"
    READY = "ready"