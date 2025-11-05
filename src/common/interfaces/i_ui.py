from typing import Protocol, Any
from src.common.enums import Rotation, Direction

class IUI(Protocol):
    """Interface for the user interface."""

    def display_board(self, board) -> None:
        """display a grid with the give height and width"""
        ...

    def display_message(self, message: str) -> None:
        """Display a message to the user."""
        ...

    def display_player_state(self, player_health: int, player_attack: int,
                             items: list[str]) -> None:
        """Display the current player state."""
        ...

    def display_game_state(self, tile, tile_position) -> None:
        """Display the current game state."""
        ...

    def get_input(self, prompt: str, options: Any) -> str:
        """Get input from the user."""
        ...

    # def get_input_with_callback(self, prompt: str, options: Any,
    #                           callback: Callable[[Any], None]) -> None:
    #     """Get input and call the callback with the result."""
    #    ...
    
    def _get_rotation_text(self, rotation: Rotation) -> str:
        """Convert rotation enum to readable text"""
        ...
