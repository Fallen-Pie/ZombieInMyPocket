import unittest
from unittest.mock import create_autospec

from src.model.game_pieces import GamePieces
from src.model.game_time.game_time import GameTime
from src.model.turn import Turn
from src.model.turn.turn_common import Triggers
from src.controller import GameController
from src.common.interfaces import IPlayer


class TestTurnAdvancement(unittest.TestCase):
    """
    Given:  the game is running
    When:   a Dev card is dawn
    Then:   time must update according to the rule of Time Passes
    """
    def setUp(self):
        """set up a turn to test"""
        self.user_interface = create_autospec(GameController)
        self.player = create_autospec(IPlayer)
        self.game_time = GameTime()
        self.game_pieces = GamePieces(self.game_time)
        self.the_turn = Turn.create(
            self.game_pieces,
            self.player,
            self.user_interface,
            self.game_time
        )
        self.the_turn.start_turn()
        self.time_before = self.game_time.get_current_time()


    def jump_to_trigger(self, trigger, result=None):
        """Jumps the turn to the given trigger"""
        self.the_turn._flow.state_finished(
            trigger=trigger,
            result=result
        )
        self.the_turn._flow._change_state()

    def test_time_not_advanced(self):
        """
        Given:  the game is running
        When:   the first dev card is dawn
        Then:   the time should not be advanced
        """
        #frist encounter
        self.jump_to_trigger(Triggers.START_ENCOUNTERS)
        self.assertEqual('get_dev_encounter', self.the_turn._flow._current_state.name.value)

        self.the_turn.continue_turn()
        self.assertEqual('run_encounter', self.the_turn._flow._current_state.name.value)
        self.assertEqual(self.time_before, self.game_time.get_current_time())


    def test_time_has_advanced(self):
        """
        Given:  the game is running
        When:   all dev cards have been dawn
        Then:   time must progress one hour
        """
        # dawn remaining dev cards
        for _ in range(10):
            self.jump_to_trigger(Triggers.START_ENCOUNTERS)
            self.the_turn.continue_turn()

        # assert time has advanced
        self.assertNotEqual(self.time_before, self.game_time.get_current_time())

if __name__ == '__main__':
    unittest.main()
