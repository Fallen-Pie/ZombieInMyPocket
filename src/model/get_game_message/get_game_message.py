from abc import ABC
from typing import Optional

from ..interfaces.i_get_game_message import IGetGameMessage
from ..interfaces.i_time import ITime

from ...enums_and_types.enums import GameStateMessage, GameInstruction, AlertMessage, UnknownErrorMessage, GameState, \
    GameOverMessage

class GetGameMessage(IGetGameMessage, ABC):
    def __init__(self, current_time: ITime) -> None:
        self.current_time = current_time
        self._state = GameState.INIT
        self._low_health = False

    def handle_game_over(self, game_over_event) -> Optional[GameOverMessage]:
        """ Retrieves message code for the end game details, based on GameOverMessage enum"""
        match game_over_event:
            # TODO: replace the string cases with actual event
            case "win event":
                # current tile is graveyard, totem is buried, time is < 12 midnight, health > 0
                return GameOverMessage.GAME_OVER_WIN
            case "lose event due to low health":
                # health is < 0
                return GameOverMessage.GAME_OVER_LOSE_HEALTH
            case "lose event due to low health":
                # time is >= 12
                return GameOverMessage.GAME_OVER_LOSE_HEALTH

    def get_state_message(self, game_event) -> Optional[GameStateMessage]:
        """Retrieves message code that constantly updates based on the players choices (i.e. room change, item selection/acquired, heal, and attack score gains  """
        # TODO: give return
        pass

    def get_current_time(self, current_time) -> int:
        # TODO: use time components to get it.
        pass

    def handle_help_key(self, current_room) -> Optional[GameInstruction]:
        """ Retrieves message code that corresponds to the current room and game state when H key is pressed"""
        match current_room:
            # TODO: replace the string cases with actual event
            case "invalid cower move":
                # find item
                return GameInstruction.STORAGE_ROOM
            case "lose event due to low health":
                # bury the totem
                return GameInstruction.GRAVEYARD
            case "lose event due to low health":
                # find the totem
                return GameInstruction.EVIL_TEMPLE
            case "lose event due to low health":
                # Choose which item to use for combat
                return GameInstruction.PICK_ATTACK_ITEM

    def handle_game_warning_event(self, game_movement, current_tile) -> Optional[AlertMessage]:
        """ Retrieves message code when triggered by game time warnings"""
        match game_movement:
            # TODO: replace the string cases with actual event
            case "invalid cower move":
                #
                return AlertMessage.INVALID_COWER_MOVE
            case "lose event due to low health":
                #
                return AlertMessage.INVALID_DOOR_EXIT_SELECTED
            case "lose event due to low health":
                #
                return AlertMessage.INVALID_COWER_MOVE
