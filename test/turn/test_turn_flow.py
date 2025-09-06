import unittest
from unittest.mock import Mock, create_autospec

#testing...
from src.model.turn import TurnFlow, State
from src.model.turn.turn_enums import Triggers, ServiceNames, ServiceMethods, StateNames

create_autospec(State, instance=True)

class MyTestCase(unittest.TestCase):
    def setUp(self):
        the_services = self.create_mock_services()
        the_transitions = self.create_mock_transitions()
        the_state = self.create_mock_states()
        self.turn_flow = TurnFlow(the_services, the_state, the_transitions)

    def create_mock_services(self):
        #mock UI
        mock_ui = Mock()
        mock_ui.get_input.return_value = 'Option1'

        #mock game
        fake_tile = Mock()
        fake_rotation = 0

        self.mock_game_pieces = Mock()
        self.mock_game_pieces.get_tile_doors.return_value = [fake_tile, fake_rotation]

        return {ServiceNames.UI:mock_ui, ServiceNames.GAME_PIECES:self.mock_game_pieces}

    def create_mock_states(self):
        pass


    @staticmethod
    def create_mock_state(name, result=None, trigger=None):
        # Create a mock that follows the State interface
        mock_state = create_autospec(State, instance=True)

        # Set attributes that would normally be initialized
        mock_state.name = name
        mock_state.result = result
        mock_state.trigger = trigger
        mock_state.context = Mock(spec=TurnFlow)  # mock context

        # Mock the abstract methods
        mock_state.enter.return_value = None
        mock_state.handle_request.return_value = None
        mock_state.exit.return_value = None

        def handle_enter_side_effect(*args, **kwargs):
            """mimics the state using a service"""
            mock_state.context.call_service_method(ServiceNames.GAME_PIECES, ServiceMethods.GET_TILE_EXITS)

        def handle_request_side_effect(*args, **kwargs):
            """this mimics the real state being called then finishing"""
            mock_state.context.state_finished(mock_state.trigger, mock_state.result)

        mock_state.handle_request.side_effect = handle_request_side_effect
        mock_state.enter.side_effect = handle_enter_side_effect

        return mock_state

    def create_mock_transitions(self):
        mock_exit_room = self.create_mock_state(StateNames.EXIT_ROOM, "door_1", Triggers.CHOOSE_DOOR)
        mock_draw_tile = self.create_mock_state(StateNames.DRAW_TILE, "fake_tile", Triggers.CHOOSE_DOOR)
        mock_choose_door = self.create_mock_state(StateNames.MOVE_PLAYER, "door_chosen", Triggers.DRAW_TILE)

        mock_transitions = {
            Triggers.EXIT_ROOM: Mock(return_value=mock_exit_room),
            Triggers.DRAW_TILE: Mock(return_value=mock_draw_tile),
            Triggers.CHOOSE_DOOR: Mock(return_value=mock_choose_door),
        }
        return mock_transitions

    def create_ready_state(self):
        return self.create_mock_state(name=StateNames.READY, result=None, trigger=Triggers.EXIT_ROOM)

    def test_starting_state_bad_day(self):
        with self.assertRaises(Exception):
            self.turn_flow.start()
        self.assertEqual(self.turn_flow._current_state, None)

    def test_starting_happy_day(self):
        #self.turn_flow.register_transition(Triggers.READY, Mock(return_value=self.create_ready_state()))
        self.assertEqual(self.turn_flow.start(), True)
        self.assertEqual(self.turn_flow._current_state.name, StateNames.READY)

    def test_calling_states(self):
        #self.turn_flow.register_transition(Triggers.READY, Mock(return_value=self.create_ready_state()))
        self.turn_flow.start()
        self.assertEqual(self.turn_flow._current_state.name, StateNames.READY)
        self.turn_flow.handle_request()
        self.assertEqual(self.turn_flow._current_state.name, StateNames.EXIT_ROOM)
        self.mock_game_pieces.get_tile_doors.assert_called()



if __name__ == '__main__':
    unittest.main()
