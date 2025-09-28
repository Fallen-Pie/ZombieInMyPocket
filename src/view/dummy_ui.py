from typing import Any, Callable
from src.enums_and_types.enums import Direction, Rotation
from .interfaces.i_ui import IUI

class DummyUI(IUI):
    
    def __init__(self):
        self.last_prompt = ""

    def display_message(self, message: str) -> None:
        print(message)

    def display_player_state(self, player_health: int, player_attack: int, 
                             items: list[str]) -> None:
        """Display the current game state"""
        print("\n=== Game Status ===")
        print(f"Health: {player_health}")
        print(f"Attack Power: {player_attack}")
        if items:
            print("Items:", ", ".join(items))
        print("=================\n")


    '''def display_game_state(self, tile, tile_position) -> None:
        """Display the current game state."""
        print("\n=== Game State ===")
        print(f"Tile: {tile}")
        print(f"Tile Position: {tile_position}")
        print("=================\n")'''                                #Add typing

    def get_input(self, prompt: str, options: Any) -> str:
        """Get input from the user with validation"""
        self.last_prompt = prompt
        valid_values = [str(i.value) for i in options]
        option_display = []

        # Probably better in view.


        for opt in options:
            if isinstance(opt, Direction):
                option_display.append(f"{opt.value} - {opt.name}")
            elif isinstance(opt, Rotation):
                option_display.append(f"{opt.value} - {self._get_rotation_text(opt)}")
            else:
                option_display.append(f"{opt.value} - {opt}")

        while True:
            print(f"\n{prompt}")
            print("Options:", ", ".join(option_display))
            user_input = input("> ").strip()
            
            if user_input in valid_values:
                return user_input
            
            print("Invalid input! Please try again.")


    def get_input_with_callback(self, prompt: str, options: Any, 
                              callback: Callable) -> None:
        """Get input and call the callback with the result"""
        result = self.get_input(prompt, options)
        callback(result)


    def _get_rotation_text(self, rotation: Rotation) -> str:
        # Getter for rotation text
        # If view houses own rotation logic should be placed here.
        return {
            Rotation.NONE: "No rotation",
            Rotation.CLOCKWISE: "Rotate 90 degrees clockwise",
            Rotation.UPSIDE_DOWN: "Rotate 180 degrees upside down",
            Rotation.ANTICLOCKWISE: "Rotate 90 degrees counterclockwise"
        }.get(rotation, str(rotation))
