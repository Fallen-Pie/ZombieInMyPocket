from src.enum.game_state_enum import GameState

class GameStateManager:
    def __init__(self):
        self.__state = GameState.INIT

        self.__current_time = 9 # treated as integer
        self.__game_over = False
        self.game_ready = False

    def start_game(self):
        if self.__state == GameState.READY:
            self.__state = GameState.RUNNING
            print("Game started!")
        else:
            print("Game is not ready to start")

    def end_game(self):
        self.__state = GameState.OVER
        print("Game over!")

    def reset_game(self):
        self.__state = GameState.READY
        print("Game is ready")

    def set_game_time(self):
        pass