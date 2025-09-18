# by Alex Lind iteration 1
from enum import Enum, auto

class GameOverConditions(Enum):
    WIN_TOTEM_BURIED = auto() # PLAYER_WON
    LOSE_PLAYER_DIED = auto() # PLAYER_DEAD
    LOSE_OUT_OF_TIME = auto() # TIME_UP
