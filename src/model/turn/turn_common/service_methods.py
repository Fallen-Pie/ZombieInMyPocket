from enum import Enum

#Change the name of service methods here
class ServiceMethods(Enum):
    """the names of the methods that states need to call from services"""
    #for player
    GET_POSITION = "get_position"
    SET_POSITION = "set_position"
    #for controller
    GET_INPUT = "get_input_with_callback"
    #for GamePieces
    GET_TILE_EXITS = "get_tile_exits"
    GET_TILE = "get_tile"
    DRAW_TILE = "draw_tile"
    IS_NEXT_TILE_NEW = "can_move_to_new_tile"
    GET_NEXT_TILE = "get_next_tile"
    PLACE_TILE = "place_tile"
    CAN_PLACE_TILE = "can_place_tile"
    GET_TILE_POSITION = "get_tile_position"
    DRAW_DEV_CARD = "draw_dev_card"
    GET_ENCOUNTER = "get_encounter"
    # for GameTime
    GET_CURRENT_TIME = "get_current_time"