"""Interface definition for turn management in Zombie in My Pocket.

This module defines the abstract base class for managing individual game turns,
including turn flow control and input handling.
"""

from abc import ABC, abstractmethod

class ITurn(ABC):
    """Abstract interface for managing game turns.
    
    Handles the flow of a single turn including initialization, execution,
    and coordination between game components and user interface.
    """

    # @classmethod
    # @abstractmethod
    # def create(cls, the_game_pieces, the_player, the_user_interface):
    #     """
    #     Create and initialize a new turn.
    #
    #     Args:
    #         the_game_pieces: The game pieces involved in the turn.
    #         the_player: The player object.
    #         the_user_interface: The user interface to handle input/output.
    #
    #     Returns:
    #         Turn: An initialized Turn instance with its turn flow set up.
    #     """
    #     pass

    @abstractmethod
    def start_turn(self) -> None:
        """
        Start a new turn.

        Sets the current state of the turn to `Ready` and begins the turn flow.
        """
        pass

    @abstractmethod
    def end_turn(self) -> None:
        """
        End the current turn.

        Stops the turn flow and resets relevant values.
        `start_turn` must be called before running a new turn.
        """
        pass

    @abstractmethod
    def continue_turn(self) -> None:
        """
        Execute the next step of the turn flow.

        This should only be called when the turn is NOT waiting for input
        (check with `is_wait_for_input`). Returns control quickly ish;
        call again if safe to proceed to the next step.
        Automatically starts a new turn after the last step.
        Use `start_turn` only before the start of first turn or after `end_turn`.
        """

    @abstractmethod
    def is_waiting_for_callback(self) -> bool:
        """
        Check if the turn is currently waiting for user input.

        Returns:
            bool: True if waiting for input, False otherwise.
        """
