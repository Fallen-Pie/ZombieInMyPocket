from enum import Enum, auto

class GameState(Enum):
    INIT = auto()
    READY = auto()
    RUNNING = auto()
    PAUSED = auto()
    OVER = auto()