from enum import Enum, auto

# Arsenie: State (From game components branch)
class GameState(Enum):
    """States outside the game play duration"""
    pass
    INIT = auto()       # Basic flow
    READY = auto()      # Basic flow
    RUNNING = auto()    # Basic flow
    PAUSED = auto()     # Alternate flow
    OVER = auto()       # Basic flow
