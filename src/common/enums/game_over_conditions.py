from enum import Enum, auto


class GameOverConditions(Enum):
    WIN_TOTEM_BURIED = auto()
    LOSE_PLAYER_DIED = auto()
    LOSE_OUT_OF_TIME = auto()