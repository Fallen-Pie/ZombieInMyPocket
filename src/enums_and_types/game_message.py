from enum import Enum

# Arsenie: [Event-driven] Game setup messages, used in get-game-status and game-state-manager.
class GameSetupMessage(Enum):
    """Messages related to game initialisation."""
    GAME_START = "Welcome Player!"
    INITIALISE = "Initialising game..."
    SHUFFLING_CARDS = "Shuffling DevCard deck..."

# Arsenie: [Event-driven] List of the game states, used in get-game-status and game-state-manager.
class GameStateMessage(Enum):
    """Codes for game state messages in the game."""
    ROOM_CHANGED = "You are now in room {}"
    TIME_CHANGE= "It is now {} PM"
    HEALTH_CHANGE = "+{} Health gained"
    ATTACK_SCORE_UPDATE = "+{} Attack score gained"
    ITEM_ACQUIRED = "You acquired a new item: {}"
    ATTACK_ITEM_SELECTED = "You picked {} item as a weapon."
    ZOMBIE_DOOR_CREATED = "Zombie Door Created!"

class GameOverMessage(Enum):
    """Messages for different game-over outcomes."""
    GAME_OVER_WIN = "Congratulations! You have won!"
    GAME_OVER_LOSE_TIME = "Oh no. You ran out of time! You have been eaten by the zombies!"
    GAME_OVER_LOSE_HEALTH = "Oh no. You are exhausted! You have been eaten by the zombies!"

class GameInstruction(Enum):
    """Codes for game tips in the game."""
    STORAGE_ROOM = "You may draw another card for a chance to get an item."
    GRAVEYARD = "Resolve a new card to bury the totem.",
    EVIL_TEMPLE = "Resolve a new card to find the totem."
    PICK_ATTACK_ITEM = "Choose item"

class AlertMessage(Enum):
    """Codes for game warnings & alerts in the game."""
    TIME_WARNING = "Hurry! Your time is running out! Burry the totem!"
    LOW_HEALTH_WARNING = "Warning! Your health is running low!"

    INVALID_COWER_MOVE = "You cannot cower during a zombie door attack"
    INVALID_DOOR_EXIT_SELECTED = "You can't enter from this side. There's no door here."
    INVALID_GRASS_PATH_SELECTED = "You can't enter from this side. Hedges block your path."

class UnknownErrorMessage(Enum):
    """Codes for system errors in the game."""
    UnknownStatusError = "Unknown system error!"


