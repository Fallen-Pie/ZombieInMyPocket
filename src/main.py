from .controller.game_controller import GameController
from .view.dummy_ui import DummyUI

def main():
    ui = DummyUI()
    game_controller = GameController(ui)
    game_controller.begin_game()

if __name__ == "__main__":
    main()
