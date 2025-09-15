import unittest
from src.model.interfaces.i_player import IPlayer
from src.model.interfaces.i_item import IItem
from src.enums_and_types.types import Position
from src.model.item.base_item import ConsumableItem
from src.model.item.combination_engine import CombinationEngine
from src.model.game_pieces import GamePieces, Tile
from src.model.interfaces.i_tile import ITile
from src.enums_and_types import Direction
from src.model.game_time.game_time import GameTime

def win_condition_player_has_totem():
    player = Player()
    player.set_has_totem(True)
    self.assertEqual(player.has_totem,True)
    
def win_condition_bury_action_avaliable():
    if self.
    self.game_pieces = GamePieces(GameTime())

def win_condition_victory_message():
    player = Player()
    is_game_over = player.check_game_over()
    self.assertEqual(is_game_over,True)
    game_over_message = turn.game_over.game_over_event()
    self.asserEqual(game_over_message, 'BURIED_TOTEM')

def win_condition_game_stop():
    turn = Turn(player)
    Player.set_has_totem(True)
    Player.bury_totem()
    has_stopped = turn.has_stopped()
    self.assertEqual(has_stopped, True)
    
def win_condition_bury_totem_unavaliable_if_totem_not_acquired():
    player = Player()
    player.bury_totem()
    self.assertEqual(player.has_burried_totem(), False)

def victory_path_can_perform_move_sequence():
    pass

def victory_path_can_achieve_victory():
    #Combat not linked to turn,
    #encounters not correctly linked to turn
    #no way to check totem placed,
    #no way to check victory
    pass

def victory_path_can_acquire_totem():
    pass
