# Map Connectivity
# - Given a generated map
# - When the player traverses all tiles with valid moves
# - Then every generated tile must be reachable from foyer tile.

from unittest import TestCase
from src.model.game_pieces import GamePieces, Tile
from src.model.interfaces.i_tile import ITile
from src.enums_and_types import Direction
from src.model.game_time.game_time import GameTime


class TestMapConnectivity(TestCase):

    def setUp(self):
        self.game_pieces = GamePieces(GameTime())

        indoor = Tile.get_indoor_tiles()
        outdoor = Tile.get_outdoor_tiles()

        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None
        self.foyer = foyer

        self.dining_room = self.get_tile(indoor, "Dining Room")
        self.game_pieces.place_tile(
            self.dining_room, Direction.SOUTH, self.foyer, Direction.NORTH)

        self.patio = self.get_tile(outdoor, "Patio")
        self.game_pieces.place_tile(
            self.patio, Direction.NORTH, self.dining_room, Direction.NORTH)

    @staticmethod
    def get_tile(tiles: list[ITile], tile_name: str) -> ITile:
        for tile in tiles:
            if tile.get_name() == tile_name:
                return tile
        assert False

    def test_first_tile_is_foyer(self):
        expected = "Foyer"
        actual = self.foyer.get_name()
        self.assertEqual(expected, actual)

    def test_can_move_to_patio(self):
        # Can move from foyer to dining room
        self.assertTrue(Direction.NORTH in self.foyer.get_exits())
        self.assertTrue(Direction.SOUTH in self.dining_room.get_exits())

        # Can move from dining room to patio
        self.assertTrue(Direction.NORTH in self.dining_room.get_exits())
        self.assertTrue(Direction.SOUTH in self.patio.get_exits())
