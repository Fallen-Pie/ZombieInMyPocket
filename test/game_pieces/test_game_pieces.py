from unittest import TestCase
from src.model.game_pieces import GamePieces, Tile
from src.enums_and_types import *
from src.model.game_time.game_time import GameTime


class TestGamePieces(TestCase):

    def setUp(self) -> None:
        self.game_pieces = GamePieces(GameTime())

        self.bathroom_tile = Tile(
            "Bathroom", False,
            (Direction.NORTH,),
            None, None)

        self.storage_tile = Tile(
            "Storage", False,
            (Direction.NORTH,),
            None, None)

        self.dining_room_tile = Tile(
            "Dining Room", False,
            (Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST),
            Direction.NORTH, None)

        self.family_room_tile = Tile(
            "Family Room", False,
            (Direction.NORTH, Direction.EAST, Direction.WEST),
            None, None)

        self.patio_tile = Tile(
            "Patio", True,
            (Direction.NORTH, Direction.EAST, Direction.SOUTH),
            Direction.NORTH, None)

        self.garden_tile = Tile(
            "Garden", True,
            (Direction.EAST, Direction.SOUTH, Direction.WEST),
            None, None)

    def test_seven_indoor_cards(self):
        self.assertEqual(self.game_pieces.indoor_tiles_remaining(), 7)

    def test_eight_outdoor_cards(self):
        self.assertEqual(self.game_pieces.outdoor_tiles_remaining(), 8)

    def test_indoor_cards_are_shuffled(self):
        first_game_pieces = GamePieces(GameTime())
        first = (
            first_game_pieces.draw_indoor_tile(),
            first_game_pieces.draw_indoor_tile(),
            first_game_pieces.draw_indoor_tile(),
        )
        second_game_pieces = GamePieces(GameTime())
        second = (
            second_game_pieces.draw_indoor_tile(),
            second_game_pieces.draw_indoor_tile(),
            second_game_pieces.draw_indoor_tile(),
        )
        self.assertNotEqual(first, second)
    
    def test_outdoor_cards_are_shuffled(self):
        first_game_pieces = GamePieces(GameTime())
        first = (
            first_game_pieces.draw_outdoor_tile(),
            first_game_pieces.draw_outdoor_tile(),
            first_game_pieces.draw_outdoor_tile(),
        )
        second_game_pieces = GamePieces(GameTime())
        second = (
            second_game_pieces.draw_outdoor_tile(),
            second_game_pieces.draw_outdoor_tile(),
            second_game_pieces.draw_outdoor_tile(),
        )
        self.assertNotEqual(first, second)
    
    def test_dev_cards_are_shuffled(self):
        first_game_pieces = GamePieces(GameTime())
        first = (
            first_game_pieces.draw_dev_card(),
            first_game_pieces.draw_dev_card(),
            first_game_pieces.draw_dev_card(),
        )
        second_game_pieces = GamePieces(GameTime())
        second = (
            second_game_pieces.draw_dev_card(),
            second_game_pieces.draw_dev_card(),
            second_game_pieces.draw_dev_card(),
        )
        self.assertNotEqual(first, second)

    def test_draw_indoor_card_decrements_count(self):
        self.game_pieces.draw_indoor_tile()
        self.assertEqual(self.game_pieces.indoor_tiles_remaining(), 6)

    def test_draw_outdoor_card_decrements_count(self):
        self.game_pieces.draw_outdoor_tile()
        self.assertEqual(self.game_pieces.outdoor_tiles_remaining(), 7)

    def test_foyer_is_at_origin(self):
        tile = self.game_pieces.get_tile((0, 0))
        assert tile is not None
        self.assertEqual(tile.get_name(), "Foyer")

    def test_can_add_upside_down_bathroom_above(self):

        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None
        self.assertTrue(self.game_pieces.can_place_tile(
            self.bathroom_tile, Direction.NORTH,
            foyer, Direction.NORTH
        ))

        self.game_pieces.place_tile(
            self.bathroom_tile, Direction.NORTH,
            foyer, Direction.NORTH
        )

        bathroom = self.game_pieces.get_tile((0, 1))
        assert bathroom is not None
        expected = "Bathroom"
        actual = bathroom.get_name()
        self.assertEqual(expected, actual)

    def test_can_not_go_out_front_door_to_indoors(self):
        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None

        self.game_pieces.place_tile(
            self.dining_room_tile, Direction.SOUTH,
            foyer, Direction.NORTH
        )
        self.assertFalse(self.game_pieces.can_place_tile(
            self.bathroom_tile, Direction.NORTH,
            self.dining_room_tile, Direction.NORTH
        ))

    def test_can_not_go_out_front_door_to_garden(self):
        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None

        self.game_pieces.place_tile(
            self.dining_room_tile, Direction.SOUTH,
            foyer, Direction.NORTH
        )
        self.assertFalse(self.game_pieces.can_place_tile(
            self.garden_tile, Direction.SOUTH,
            self.dining_room_tile, Direction.NORTH
        ))

    def test_can_go_out_front_door_to_patio(self):
        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None

        self.game_pieces.place_tile(
            self.dining_room_tile, Direction.SOUTH,
            foyer, Direction.NORTH
        )
        self.assertTrue(self.game_pieces.can_place_tile(
            self.patio_tile, Direction.NORTH,
            self.dining_room_tile, Direction.NORTH
        ))

    def test_can_not_go_out_front_door_to_patio_not_rotated(self):
        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None

        self.game_pieces.place_tile(
            self.dining_room_tile, Direction.SOUTH,
            foyer, Direction.NORTH
        )
        self.assertFalse(self.game_pieces.can_place_tile(
            self.patio_tile, Direction.SOUTH,
            self.dining_room_tile, Direction.NORTH
        ))

    def test_is_stuck_starts_false(self):
        self.assertFalse(self.game_pieces.is_stuck())

    def test_is_stuck_is_true_with_bathroom_above(self):
        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None
        self.game_pieces.place_tile(
            self.bathroom_tile, Direction.NORTH,
            foyer, Direction.NORTH
        )
        self.assertTrue(self.game_pieces.is_stuck())

    def test_complex_stuck_scenario(self):
        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None

        self.game_pieces.place_tile(
            self.family_room_tile, Direction.NORTH,
            foyer, Direction.NORTH
        )
        self.game_pieces.place_tile(
            self.bathroom_tile, Direction.NORTH,
            self.family_room_tile, Direction.EAST
        )

        self.assertFalse(self.game_pieces.is_stuck())

        self.game_pieces.place_tile(
            self.storage_tile, Direction.NORTH,
            self.family_room_tile, Direction.WEST
        )
        self.assertTrue(self.game_pieces.is_stuck())

    def test_get_tile_position(self):
        foyer = self.game_pieces.get_tile((0, 0))
        assert foyer is not None
        self.assertTrue(self.game_pieces.can_place_tile(
            self.bathroom_tile, Direction.NORTH,
            foyer, Direction.NORTH
        ))
        self.game_pieces.place_tile(
            self.bathroom_tile, Direction.NORTH,
            foyer, Direction.NORTH
        )
        expected = (0, 1)
        actual = self.game_pieces.get_tile_position(self.bathroom_tile)
        self.assertTrue(expected, actual)


if __name__ == '__main__':
    import unittest
    unittest.main()
