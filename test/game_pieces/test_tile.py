import unittest
from src.enums_and_types import *
from src.model.game_pieces.tile import OutdoorTile
from src.model.game_pieces.tile_builder import IndoorTileBuilder, OutdoorTileBuilder
from src.model.game_pieces.tile_director import TileDirector


class TestTile(unittest.TestCase):

    def setUp(self) -> None:
        tile_director = TileDirector()

        builder = IndoorTileBuilder()
        tile_director.set_builder(builder)
        tile_director.build_minimal_tite("Family Room",
            (Direction.WEST, Direction.NORTH, Direction.EAST))
        self.family_room_tile = builder.product

        builder = OutdoorTileBuilder()
        tile_director.set_builder(builder)
        tile_director.build_tite_with_exit("Patio",
            (Direction.NORTH, Direction.EAST, Direction.SOUTH), Direction.NORTH)
        self.patio_tile = builder.product

    def test_get_name(self):
        self.assertEqual(self.family_room_tile.get_name(), "Family Room")

    def test_is_outdoors(self):
        self.assertTrue(isinstance(self.patio_tile, OutdoorTile))
        self.assertFalse(isinstance(self.family_room_tile, OutdoorTile))

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
