from typing import Callable, Any
from threading import Timer
from src.enums_and_types import enums

class UserInterface:
    """A mock user interface."""
    def get_input_with_callback(self, prompt: str, options: Any, callback: Callable[[Any], None]) -> None:
        """adds mock callback behavior."""
        def delay_call():
            result = self.get_input(prompt, options)
            callback(result)
        Timer(1, delay_call).start()

    @staticmethod
    def get_input(prompt: str, options: Any) -> str:
        valid_values = [str(o.value) for o in options]
        user_input = ""
        while user_input not in valid_values:
            user_input = input(f"{prompt}, {valid_values}: ")
        return user_input