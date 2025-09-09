from src.enums_and_types.enums import GameState


class GameSessionManager:
    """ Handles game states and set up. """
    def __init__(self):
        """ Coordinates the state and the components of the game (Time, Turn, Player, and GameOver/GameStatus)"""
        self._current_state = GameState.INIT
        self.health = 6 #TODO: replace with actual method/interface that get these values
        self.attack = 1  #TODO: replace with actual method/interface that get these values
        self.room = "Foyer" #TODO: replace with actual method/interface that get these values

    def set_current_state(self, state:GameState):
        """ Event-driven command that updates game states"""
        if not isinstance(state, GameState):
            raise ValueError("Invalid game state")
        self._current_state = state

    def get_current_state(self):
        return self._current_state

    def setup_game(self):
        """"""
        # set_current_state
        # set_game_time
        pass

    def start_game(self):
        """"""
        pass

    def end_game(self):
        """ Handles stopping game operations. """
        pass

    def reset_game(self):
        """Resets game values"""
        # TODO: handle clear_tiles
        self.health = 6
        self.attack = 1
        self.room = "Foyer"
        self._current_state = GameState.INIT

    def save_game(self):
        """ Save game progress """
        pass

    def load_game(self):
        """ Restore saved game progress """
        pass