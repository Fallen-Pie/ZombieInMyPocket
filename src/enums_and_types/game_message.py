from enum import Enum

# class MessageCategory(Enum):
#     EVENT = "event_triggered"
#     KEY = "key_triggered"

# class EventMessage(Enum):
#     GAME_STATE = "Game update: {0}"
#     ALERT = "⚠ Alert: {0}"
#     FEEDBACK = "⚠ Update: {0}"
#     INVALID_MOVE = "Invalid move: {0}"
#
# class KeyMessage(Enum):
#     TOOLTIP = "Info: {0}"
#     STATISTICS = "Stats → Health: {0}, Attack: {1}, Time: {2}, Room: {3}"

class MessageType(Enum):
    STATUS = "Game update: {0}"             # Persistent state (time, health, room updates)
    ALERT = "⚠ Alert: {0}"                  # Urgent warning (low health, invalid move, etc.)
    FEEDBACK = "⚠ Update: {0}"              # General events (items acquired, score gained) and Actions (draw card, grab item, etc.)

    TOOLTIP = "Info: {0}"                   # Tips, prompts, or guidance
    STATISTICS = "Stats → Health: {0}, Attack: {1}, Time: {2}, Room: {3}"

# Arsenie: [Event-driven] Game setup messages, used in get-game-status and game-state-manager.
class GameSetupMessage(Enum):
    """Feedback Messages related to game initialisation."""
    GAME_START = "Welcome Player! You are in room {0}"
    INITIALISE = "Initialising game..."
    SHUFFLING_CARDS = "Shuffling DevCard deck..."

# Arsenie: [Event-driven] List of the game states, used in get-game-status and game-state-manager.
class GameFeedbackMessage(Enum):
    """Feedback Message Codes for changes in the game triggerred by the user."""
    TIME_CHANGE= "It is now {} PM"
    ROOM_CHANGED = "You are now in room {}"
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

class ErrorMessage(Enum):
    """Codes for system errors in the game."""
    UnknownStatusError = "Unknown system error!"