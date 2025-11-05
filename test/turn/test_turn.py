import unittest
from unittest.mock import create_autospec


from src.model.turn.turn_common import Triggers
from src.model import Player, GameTime, GamePieces, Turn
from src.controller import GameController



class TestTurn(unittest.TestCase):
    """tests for Turn (context and states"""
    def setUp(self):
        """set up a turn to test"""
        self.user_interface = create_autospec(GameController)
        self.player = create_autospec(Player())
        self.game_time = create_autospec(GameTime())
        self.game_pieces = create_autospec(GamePieces(self.game_time))
        self.the_turn = Turn.create(
            self.game_pieces,
            self.player,
            self.user_interface,
            self.game_time
        )


    def jump_to_trigger(self, trigger, result = None):
        """Jumps the turn to the given trigger"""
        self.the_turn._flow.state_finished(
            trigger = trigger,
            result = result
        )
        self.the_turn._flow._change_state()


    def assert_turn_reset(self):
        """
        Assert that the turn is in a fully reset state:
        no active state in the flow
        waiting for a callback
        cannot be continued
        """
        self.assertIsNone(self.the_turn._flow._current_state)
        self.assertTrue(self.the_turn.is_waiting_for_callback())
        with self.assertRaisesRegex(RuntimeError, "Cannot continue turn while waiting for input."):
            self.the_turn.continue_turn()


    def test_turn_before_start(self):
        """
        given:  a new Turn instance
        when:   no actions have been taken
        then:   the turn should be in a reset state
        """
        self.assert_turn_reset()


    def test_turn_start(self):
        """
        given:  the turn is ready to start
        when:   the game_manger starts the turn
        Then:   the turn should be in the ready state
        """
        self.the_turn.start_turn()
        self.assertEqual(self.the_turn._flow._current_state.name.value, 'ready')
        self.assertFalse(self.the_turn.is_waiting_for_callback())


    def test_continue_turn(self):
        """
        given:  the turn has started
        when:   the turn continues
        Then:   the turn should continue to the next state
        """
        self.the_turn.start_turn()
        self.the_turn.continue_turn()
        self.assertEqual(self.the_turn._flow._current_state.name.value, 'get_player_tile')

        self.jump_to_trigger(Triggers.START_ENCOUNTERS)

        self.assertEqual('get_dev_encounter', self.the_turn._flow._current_state.name.value)
        self.the_turn.continue_turn()
        self.assertEqual('run_encounter', self.the_turn._flow._current_state.name.value)


    def test_turn_after_end(self):
        """
        given:  the turn is active
        when:   the turn is ended
        Then:   the turn should reset to its initial state
        """
        self.the_turn.start_turn()
        self.the_turn.continue_turn()
        self.the_turn.continue_turn()
        self.the_turn.end_turn()
        self.assert_turn_reset()


if __name__ == '__main__':
    unittest.main()
