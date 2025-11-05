from typing import Callable, Any

from src.common.interfaces import ITurn

from src.model.turn.turn_common import ServiceNames, StateNames, Triggers
from src.model.turn.turn_flow import TurnFlow
from src.model.turn.turn_states import *



class Turn(ITurn):
    """
    Controls the flow of a turn from start to finish by calling on other
    components in order to progress the turn.

    Responsibilities:
        Coordinate with other components to advance the turn
        Calls for input from the user in some cases

    Limitations:
        Does not decide win/loss conditions.
        Does not decide whether the turn should continue after each step.
            These decisions should be handled by other components.
        Returns control frequently to allow higher-level checks.
    """
    def __init__(self, flow):
        self._flow: TurnFlow = flow

    #make the turn flow object
    @classmethod
    def create(
            cls, the_game_pieces, the_player, the_user_interface, the_game_time
    ) -> ITurn:
        """
        Create and initialize a new turn.

        Args:
            the_game_pieces: The game pieces involved in the turn.
            the_player: The player object.
            the_user_interface: The user interface to handle input/output.
            the_game_time: The game time, optional for compatibility only.

        Returns:
            Turn: An initialized Turn instance with its turn flow set up.
        """
        services = cls._get_services(
            the_game_pieces,
            the_player,
            the_user_interface,
            the_game_time
        )

        states = cls._get_turn_states()

        transitions = cls._get_transitions()

        flow = TurnFlow(
            the_services=services,
            the_states=states,
            the_transitions=transitions
        )

        return cls(flow)

    @classmethod
    def _get_services(
            cls,
            the_game_pieces,
            the_player,
            the_controller,
            the_game_time
    ) -> dict[ServiceNames, object]:
        """Get the services used by the turn"""
        return {
            ServiceNames.GAME_PIECES:   the_game_pieces,
            ServiceNames.PLAYER:        the_player,
            ServiceNames.CONTROLLER:    the_controller,
            ServiceNames.GAME_TIME:     the_game_time
        }

    @classmethod
    def _get_turn_states(cls) -> dict[StateNames, Callable[[], Any]]:
        """Get the states used by the turn"""
        return {
            StateNames.READY:               lambda: Ready(),
            StateNames.GET_PLAYER_TILE:     lambda: GetPlayerTile(),
            StateNames.SELECT_EXIT:         lambda: SelectExit(),
            StateNames.CHECK_NEXT_TILE:     lambda: CheckNextTile(),
            StateNames.DRAW_TILE:           lambda: DrawTile(),
            StateNames.PLACE_TILE:          lambda: PlaceTile(),
            StateNames.MOVE_PLAYER:         lambda: MovePlayer(),
            StateNames.GET_DEV_ENCOUNTER:   lambda: GetDevEncounter(),
            StateNames.GET_TILE_ENCOUNTER:  lambda: GetTileEncounter(),
            StateNames.GET_COWER_ENCOUNTER: lambda: GetCowerEncounter(),
            StateNames.RUN_ENCOUNTER:       lambda: RunEncounter(),

        }

    @classmethod
    def _get_transitions(cls) -> dict[Triggers, StateNames]:
        """Get the transitions used by the turn"""
        return {
            # Trigger,                       #Next State
            Triggers.READY:                 StateNames.READY,

            Triggers.START_TURN:            StateNames.GET_PLAYER_TILE,
            Triggers.SELECT_EXIT:           StateNames.SELECT_EXIT,

            Triggers.DRAW_TILE:             StateNames.DRAW_TILE,
            Triggers.MOVE_PLAYER:           StateNames.MOVE_PLAYER,

            Triggers.NEW_TILE_EXIT:         StateNames.PLACE_TILE,
            Triggers.PLAYER_TILE_EXIT:      StateNames.CHECK_NEXT_TILE,

            Triggers.START_ENCOUNTERS:      StateNames.GET_DEV_ENCOUNTER,

            Triggers.RUN_ENCOUNTER:         StateNames.RUN_ENCOUNTER,

            Triggers.DEV_ENCOUNTER_END:     StateNames.GET_PLAYER_TILE,
            Triggers.START_TILE_ENCOUNTER:  StateNames.GET_TILE_ENCOUNTER,
            Triggers.TILE_ENCOUNTER_END:    StateNames.GET_COWER_ENCOUNTER,
            Triggers.COWER_ENCOUNTER_END:   StateNames.READY,

        }

    #interface for turn
    def start_turn(self) -> None:
        """
        Start a new turn.

        Sets the current state of the turn to `Ready` and begins the turn flow.
        """
        self._flow.start_turn()

    def end_turn(self) -> None:
        """
        End the current turn.

        Stops the turn flow and resets relevant values.
        `start_turn` must be called before running a new turn.
        """
        self._flow.end_turn()

    def continue_turn(self) -> None:
        """
        Execute the next step of the turn flow.

        This should only be called when the turn is NOT waiting for input
        (check with `is_wait_for_input`). Returns control quickly ish;
        call again if safe to proceed to the next step.
        Automatically starts a new turn after the last step.
        Use `start_turn` only before the start of first turn or after `end_turn`.
        """
        if self._flow.is_waiting_for_callback():
            raise RuntimeError("Cannot continue turn while waiting for input.")
        self._flow.continue_turn()

    def is_waiting_for_callback(self) -> bool:
        """
        Check if the turn is currently waiting for user input.

        Returns:
            bool: True if waiting for input, False otherwise.
        """
        return self._flow.is_waiting_for_callback()
