import os

# if os.getenv("RUNNING_TURN_TESTS") == "1":
#     #running tests for the turn packages only
#     #set environment variable to "RUNNING_TURN_TESTS=1"
#     from .turn import State #, TurnFlow
#     from .turn.turn_states import *
#
#     __all__ = [
#         #'TurnFlow',
#         'State',
#     ]

#else: #not testing
from .player import Player
from .game_pieces import GamePieces, DevCard, Tile
from .turn import Turn
#from .turn import TurnSetUp #,TurnFlow

__all__ = [
    'Player',
    'GamePieces',
    'DevCard',
    'Tile',
    'Turn'
]
