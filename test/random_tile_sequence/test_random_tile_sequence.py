# Random Tile Sequence
# - Given a new game starts
# - When the player explores six tiles
# - Then the sequence of generated tile and/or types should
#   be different from another new game

from unittest import TestCase
from src.model.game_pieces import GamePieces
from src.model.game_time.game_time import GameTime


class TestRandomTileSequence(TestCase):

    def setUp(self):
        self.game_pieces = GamePieces(GameTime())

    def get_six_tiles(self, is_outdoor: bool) -> list[str]:
        self.setUp()
        result: list[str] = []
        for _ in range(6):
            if is_outdoor:
                tile = self.game_pieces.draw_outdoor_tile()
            else:
                tile = self.game_pieces.draw_indoor_tile()
            result.append(tile.get_name())
        print(result)
        return result

    def get_six_indoor_tiles(self) -> list[str]:
        return self.get_six_tiles(False)

    def get_six_outdoor_tiles(self) -> list[str]:
        return self.get_six_tiles(True)

    def test_six_indoor_tiles_are_different(self):
        first = self.get_six_indoor_tiles()
        second = self.get_six_indoor_tiles()
        self.assertNotEqual(first, second)

    def test_six_outdoor_tiles_are_different(self):
        first = self.get_six_outdoor_tiles()
        second = self.get_six_outdoor_tiles()
        self.assertNotEqual(first, second)
