from src.model.game_pieces import Tile
import unittest
from src.enums_and_types import *


class TestTile(unittest.TestCase):

    def setUp(self) -> None:
        self.family_room_tile = Tile(
            "Family Room",
            False,
            (Direction.WEST, Direction.NORTH, Direction.EAST),
            None,
            None
        )

        self.patio_tile = Tile(
            "Patio",
            True,
            (Direction.NORTH, Direction.EAST, Direction.SOUTH),
            Direction.NORTH,
            None
        )

    def test_get_name(self):
        self.assertEqual(self.family_room_tile.get_name(), "Family Room")

    def test_is_outdoors(self):
        self.assertTrue(self.patio_tile.is_outdoors())
        self.assertFalse(self.family_room_tile.is_outdoors())

    def test_get_exits_no_rotation(self):
        self.family_room_tile.set_rotation(Rotation.NONE)
        self.assertIn(Direction.WEST,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.NORTH,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.EAST,
                      self.family_room_tile.get_exits())
        self.assertNotIn(Direction.SOUTH,
                         self.family_room_tile.get_exits())

    def test_get_exits_clockwise(self):
        self.family_room_tile.set_rotation(Rotation.CLOCKWISE)
        self.assertIn(Direction.NORTH,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.EAST,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.SOUTH,
                      self.family_room_tile.get_exits())
        self.assertNotIn(Direction.WEST,
                         self.family_room_tile.get_exits())

    def test_get_exits_anticlockwise(self):
        self.family_room_tile.set_rotation(Rotation.ANTICLOCKWISE)
        self.assertIn(Direction.SOUTH,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.WEST,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.NORTH,
                      self.family_room_tile.get_exits())
        self.assertNotIn(Direction.EAST,
                         self.family_room_tile.get_exits())

    def test_get_exits_upside_down(self):
        self.family_room_tile.set_rotation(Rotation.UPSIDE_DOWN)
        self.assertIn(Direction.EAST,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.SOUTH,
                      self.family_room_tile.get_exits())
        self.assertIn(Direction.WEST,
                      self.family_room_tile.get_exits())
        self.assertNotIn(Direction.NORTH,
                         self.family_room_tile.get_exits())

    def test_get_front_door_no_rotation(self):
        self.assertIsNone(self.family_room_tile.get_front_door())

        self.patio_tile.set_rotation(Rotation.NONE)
        self.assertEqual(self.patio_tile.get_front_door(),
                         Direction.NORTH)

    def test_get_front_door_clockwise(self):
        self.patio_tile.set_rotation(Rotation.CLOCKWISE)
        self.assertEqual(self.patio_tile.get_front_door(),
                         Direction.EAST)

    def test_get_front_door_anticlockwise(self):
        self.patio_tile.set_rotation(Rotation.ANTICLOCKWISE)
        self.assertEqual(self.patio_tile.get_front_door(),
                         Direction.WEST)

    def test_get_front_door_upside_down(self):
        self.patio_tile.set_rotation(Rotation.UPSIDE_DOWN)
        self.assertEqual(self.patio_tile.get_front_door(),
                         Direction.SOUTH)
