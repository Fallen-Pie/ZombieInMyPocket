from enum import Enum, auto

# class GameState(Enum):
#     """States outside the game play duration"""
#     pass
#     INIT = auto()       # Basic flow
#     READY = auto()      # Basic flow
#     RUNNING = auto()    # Basic flow
#     PAUSED = auto()     # Alternate flow
#     OVER = auto()       # Basic flow

class GameState(Enum):
    INIT = "init"
    EXPLORING = "exploring"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    VICTORY = "victory"
