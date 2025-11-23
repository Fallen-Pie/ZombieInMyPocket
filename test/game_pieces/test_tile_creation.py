"""
Test suite for tile.py tile creation methods.

This module tests all observable external behaviors of:
- get_indoor_tiles() (lines 50-86)
- get_outdoor_tiles() (lines 88-124)

Tests cover all 16 tiles created by these factory methods to achieve
100% coverage of the target code block.

Can be run standalone:
    python -m unittest test.game_pieces.test_tile_creation

Or with coverage:
    coverage run -m unittest test.game_pieces.test_tile_creation
    coverage html --include="src/model/game_pieces/tile.py"
"""
import unittest
from src.model.game_pieces.tile import Tile
from src.enums_and_types import Direction
from src.model.encounters.item_encounter import ItemEncounter
from src.model.encounters.health_encounter import HealthEncounter
from src.model.encounters.not_implemented_encounters import TotemEncounter


class TestGetIndoorTiles(unittest.TestCase):
    """Test get_indoor_tiles() factory method."""

    def setUp(self):
        """Set up test fixtures."""
        self.tiles = Tile.get_indoor_tiles()

    def test_returns_list_of_tiles(self):
        """Test get_indoor_tiles returns a list."""
        self.assertIsInstance(self.tiles, list)

    def test_returns_eight_tiles(self):
        """Test get_indoor_tiles returns exactly 8 tiles."""
        self.assertEqual(len(self.tiles), 8)

    def test_all_tiles_are_indoor(self):
        """Test all tiles returned have is_outdoors() == False."""
        for tile in self.tiles:
            with self.subTest(tile=tile.get_name()):
                self.assertFalse(tile.is_outdoors())

    def test_all_tiles_have_names(self):
        """Test all tiles have non-empty names."""
        for tile in self.tiles:
            with self.subTest(tile=tile.get_name()):
                self.assertIsInstance(tile.get_name(), str)
                self.assertGreater(len(tile.get_name()), 0)

    def test_bathroom_tile_exists(self):
        """Test Bathroom tile is in indoor tiles."""
        bathroom = self._get_tile_by_name("Bathroom")
        self.assertIsNotNone(bathroom)

    def test_bathroom_tile_properties(self):
        """Test Bathroom tile has correct properties."""
        bathroom = self._get_tile_by_name("Bathroom")
        self.assertIsNotNone(bathroom)
        assert bathroom is not None  # Type narrowing for Pylance
        self.assertFalse(bathroom.is_outdoors())
        self.assertIn(Direction.NORTH, bathroom.get_exits())
        self.assertEqual(len(bathroom.get_exits()), 1)
        self.assertIsNone(bathroom.get_front_door())
        self.assertIsNone(bathroom.get_encounter())

    def test_kitchen_tile_exists(self):
        """Test Kitchen tile is in indoor tiles."""
        kitchen = self._get_tile_by_name("Kitchen")
        self.assertIsNotNone(kitchen)

    def test_kitchen_tile_properties(self):
        """Test Kitchen tile has correct properties."""
        kitchen = self._get_tile_by_name("Kitchen")
        self.assertIsNotNone(kitchen)
        assert kitchen is not None  # Type narrowing for Pylance
        self.assertFalse(kitchen.is_outdoors())
        exits = kitchen.get_exits()
        self.assertIn(Direction.NORTH, exits)
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 3)
        self.assertIsNone(kitchen.get_front_door())
        self.assertIsInstance(kitchen.get_encounter(), HealthEncounter)

    def test_storage_tile_exists(self):
        """Test Storage tile is in indoor tiles."""
        storage = self._get_tile_by_name("Storage")
        self.assertIsNotNone(storage)

    def test_storage_tile_properties(self):
        """Test Storage tile has correct properties."""
        storage = self._get_tile_by_name("Storage")
        self.assertIsNotNone(storage)
        assert storage is not None  # Type narrowing for Pylance
        self.assertFalse(storage.is_outdoors())
        self.assertIn(Direction.NORTH, storage.get_exits())
        self.assertEqual(len(storage.get_exits()), 1)
        self.assertIsNone(storage.get_front_door())
        self.assertIsInstance(storage.get_encounter(), ItemEncounter)

    def test_evil_temple_tile_exists(self):
        """Test Evil Temple tile is in indoor tiles."""
        temple = self._get_tile_by_name("Evil Temple")
        self.assertIsNotNone(temple)

    def test_evil_temple_tile_properties(self):
        """Test Evil Temple tile has correct properties."""
        temple = self._get_tile_by_name("Evil Temple")
        self.assertIsNotNone(temple)
        assert temple is not None  # Type narrowing for Pylance
        self.assertFalse(temple.is_outdoors())
        exits = temple.get_exits()
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 2)
        self.assertIsNone(temple.get_front_door())
        self.assertIsInstance(temple.get_encounter(), TotemEncounter)

    def test_family_room_tile_exists(self):
        """Test Family Room tile is in indoor tiles."""
        family_room = self._get_tile_by_name("Family Room")
        self.assertIsNotNone(family_room)

    def test_family_room_tile_properties(self):
        """Test Family Room tile has correct properties."""
        family_room = self._get_tile_by_name("Family Room")
        self.assertIsNotNone(family_room)
        assert family_room is not None  # Type narrowing for Pylance
        self.assertFalse(family_room.is_outdoors())
        exits = family_room.get_exits()
        self.assertIn(Direction.NORTH, exits)
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 3)
        self.assertIsNone(family_room.get_front_door())
        self.assertIsNone(family_room.get_encounter())

    def test_dining_room_tile_exists(self):
        """Test Dining Room tile is in indoor tiles."""
        dining_room = self._get_tile_by_name("Dining Room")
        self.assertIsNotNone(dining_room)

    def test_dining_room_tile_properties(self):
        """Test Dining Room tile has correct properties."""
        dining_room = self._get_tile_by_name("Dining Room")
        self.assertIsNotNone(dining_room)
        assert dining_room is not None  # Type narrowing for Pylance
        self.assertFalse(dining_room.is_outdoors())
        exits = dining_room.get_exits()
        self.assertIn(Direction.NORTH, exits)
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.SOUTH, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 4)
        self.assertEqual(dining_room.get_front_door(), Direction.NORTH)
        self.assertIsNone(dining_room.get_encounter())

    def test_bedroom_tile_exists(self):
        """Test Bedroom tile is in indoor tiles."""
        bedroom = self._get_tile_by_name("Bedroom")
        self.assertIsNotNone(bedroom)

    def test_bedroom_tile_properties(self):
        """Test Bedroom tile has correct properties."""
        bedroom = self._get_tile_by_name("Bedroom")
        self.assertIsNotNone(bedroom)
        assert bedroom is not None  # Type narrowing for Pylance
        self.assertFalse(bedroom.is_outdoors())
        exits = bedroom.get_exits()
        self.assertIn(Direction.NORTH, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 2)
        self.assertIsNone(bedroom.get_front_door())
        self.assertIsNone(bedroom.get_encounter())

    def test_foyer_tile_exists(self):
        """Test Foyer tile is in indoor tiles."""
        foyer = self._get_tile_by_name("Foyer")
        self.assertIsNotNone(foyer)

    def test_foyer_tile_properties(self):
        """Test Foyer tile has correct properties."""
        foyer = self._get_tile_by_name("Foyer")
        self.assertIsNotNone(foyer)
        assert foyer is not None  # Type narrowing for Pylance
        self.assertFalse(foyer.is_outdoors())
        self.assertIn(Direction.NORTH, foyer.get_exits())
        self.assertEqual(len(foyer.get_exits()), 1)
        self.assertIsNone(foyer.get_front_door())
        self.assertIsNone(foyer.get_encounter())

    def test_all_indoor_tile_names_present(self):
        """Test all expected indoor tile names are present."""
        expected_names = [
            "Bathroom", "Kitchen", "Storage", "Evil Temple",
            "Family Room", "Dining Room", "Bedroom", "Foyer"
        ]
        actual_names = [tile.get_name() for tile in self.tiles]
        for name in expected_names:
            with self.subTest(tile_name=name):
                self.assertIn(name, actual_names)

    def _get_tile_by_name(self, name: str):
        """Helper method to get tile by name."""
        for tile in self.tiles:
            if tile.get_name() == name:
                return tile
        return None


class TestGetOutdoorTiles(unittest.TestCase):
    """Test get_outdoor_tiles() factory method."""

    def setUp(self):
        """Set up test fixtures."""
        self.tiles = Tile.get_outdoor_tiles()

    def test_returns_list_of_tiles(self):
        """Test get_outdoor_tiles returns a list."""
        self.assertIsInstance(self.tiles, list)

    def test_returns_eight_tiles(self):
        """Test get_outdoor_tiles returns exactly 8 tiles."""
        self.assertEqual(len(self.tiles), 8)

    def test_all_tiles_are_outdoor(self):
        """Test all tiles returned have is_outdoors() == True."""
        for tile in self.tiles:
            with self.subTest(tile=tile.get_name()):
                self.assertTrue(tile.is_outdoors())

    def test_all_tiles_have_names(self):
        """Test all tiles have non-empty names."""
        for tile in self.tiles:
            with self.subTest(tile=tile.get_name()):
                self.assertIsInstance(tile.get_name(), str)
                self.assertGreater(len(tile.get_name()), 0)

    def test_garden_tile_exists(self):
        """Test Garden tile is in outdoor tiles."""
        garden = self._get_tile_by_name("Garden")
        self.assertIsNotNone(garden)

    def test_garden_tile_properties(self):
        """Test Garden tile has correct properties."""
        garden = self._get_tile_by_name("Garden")
        self.assertIsNotNone(garden)
        assert garden is not None  # Type narrowing for Pylance
        self.assertTrue(garden.is_outdoors())
        exits = garden.get_exits()
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.SOUTH, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 3)
        self.assertIsNone(garden.get_front_door())
        self.assertIsInstance(garden.get_encounter(), HealthEncounter)

    def test_sitting_area_tile_exists(self):
        """Test Sitting Area tile is in outdoor tiles."""
        sitting_area = self._get_tile_by_name("Sitting Area")
        self.assertIsNotNone(sitting_area)

    def test_sitting_area_tile_properties(self):
        """Test Sitting Area tile has correct properties."""
        sitting_area = self._get_tile_by_name("Sitting Area")
        self.assertIsNotNone(sitting_area)
        assert sitting_area is not None  # Type narrowing for Pylance
        self.assertTrue(sitting_area.is_outdoors())
        exits = sitting_area.get_exits()
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.SOUTH, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 3)
        self.assertIsNone(sitting_area.get_front_door())
        self.assertIsNone(sitting_area.get_encounter())

    def test_yard_tiles_exist(self):
        """Test Yard tiles are in outdoor tiles (3 instances)."""
        yards = [tile for tile in self.tiles if tile.get_name() == "Yard"]
        self.assertEqual(len(yards), 3)

    def test_yard_tile_properties(self):
        """Test Yard tiles have correct properties."""
        yards = [tile for tile in self.tiles if tile.get_name() == "Yard"]
        for yard in yards:
            with self.subTest(yard_instance=yards.index(yard)):
                self.assertTrue(yard.is_outdoors())
                exits = yard.get_exits()
                self.assertIn(Direction.EAST, exits)
                self.assertIn(Direction.SOUTH, exits)
                self.assertIn(Direction.WEST, exits)
                self.assertEqual(len(exits), 3)
                self.assertIsNone(yard.get_front_door())
                self.assertIsNone(yard.get_encounter())

    def test_graveyard_tile_exists(self):
        """Test Graveyard tile is in outdoor tiles."""
        graveyard = self._get_tile_by_name("Graveyard")
        self.assertIsNotNone(graveyard)

    def test_graveyard_tile_properties(self):
        """Test Graveyard tile has correct properties."""
        graveyard = self._get_tile_by_name("Graveyard")
        self.assertIsNotNone(graveyard)
        assert graveyard is not None  # Type narrowing for Pylance
        self.assertTrue(graveyard.is_outdoors())
        exits = graveyard.get_exits()
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.SOUTH, exits)
        self.assertEqual(len(exits), 2)
        self.assertIsNone(graveyard.get_front_door())
        self.assertIsNone(graveyard.get_encounter())

    def test_garage_tile_exists(self):
        """Test Garage tile is in outdoor tiles."""
        garage = self._get_tile_by_name("Garage")
        self.assertIsNotNone(garage)

    def test_garage_tile_properties(self):
        """Test Garage tile has correct properties."""
        garage = self._get_tile_by_name("Garage")
        self.assertIsNotNone(garage)
        assert garage is not None  # Type narrowing for Pylance
        self.assertTrue(garage.is_outdoors())
        exits = garage.get_exits()
        self.assertIn(Direction.SOUTH, exits)
        self.assertIn(Direction.WEST, exits)
        self.assertEqual(len(exits), 2)
        self.assertIsNone(garage.get_front_door())
        self.assertIsNone(garage.get_encounter())

    def test_patio_tile_exists(self):
        """Test Patio tile is in outdoor tiles."""
        patio = self._get_tile_by_name("Patio")
        self.assertIsNotNone(patio)

    def test_patio_tile_properties(self):
        """Test Patio tile has correct properties."""
        patio = self._get_tile_by_name("Patio")
        self.assertIsNotNone(patio)
        assert patio is not None  # Type narrowing for Pylance
        self.assertTrue(patio.is_outdoors())
        exits = patio.get_exits()
        self.assertIn(Direction.NORTH, exits)
        self.assertIn(Direction.EAST, exits)
        self.assertIn(Direction.SOUTH, exits)
        self.assertEqual(len(exits), 3)
        self.assertEqual(patio.get_front_door(), Direction.NORTH)
        self.assertIsNone(patio.get_encounter())

    def _get_tile_by_name(self, name: str):
        """Helper method to get tile by name."""
        for tile in self.tiles:
            if tile.get_name() == name:
                return tile
        return None


class TestTileCreationIntegration(unittest.TestCase):
    """Integration tests for tile creation methods."""

    def test_indoor_tiles_returns_new_instances_each_call(self):
        """Test get_indoor_tiles returns new instances on each call."""
        tiles1 = Tile.get_indoor_tiles()
        tiles2 = Tile.get_indoor_tiles()
        # Different list instances
        self.assertIsNot(tiles1, tiles2)
        # Same length
        self.assertEqual(len(tiles1), len(tiles2))

    def test_outdoor_tiles_returns_new_instances_each_call(self):
        """Test get_outdoor_tiles returns new instances on each call."""
        tiles1 = Tile.get_outdoor_tiles()
        tiles2 = Tile.get_outdoor_tiles()
        # Different list instances
        self.assertIsNot(tiles1, tiles2)
        # Same length
        self.assertEqual(len(tiles1), len(tiles2))

    def test_total_tiles_available(self):
        """Test total number of tiles from both methods."""
        indoor = Tile.get_indoor_tiles()
        outdoor = Tile.get_outdoor_tiles()
        total = len(indoor) + len(outdoor)
        self.assertEqual(total, 16)

    def test_no_tile_is_both_indoor_and_outdoor(self):
        """Test tiles are either indoor or outdoor, not both."""
        indoor = Tile.get_indoor_tiles()
        outdoor = Tile.get_outdoor_tiles()
        for tile in indoor:
            self.assertFalse(tile.is_outdoors())
        for tile in outdoor:
            self.assertTrue(tile.is_outdoors())

    def test_tiles_with_front_doors(self):
        """Test only specific tiles have front doors."""
        indoor = Tile.get_indoor_tiles()
        outdoor = Tile.get_outdoor_tiles()
        all_tiles = indoor + outdoor

        tiles_with_doors = [
            tile for tile in all_tiles
            if tile.get_front_door() is not None
        ]
        # Only Dining Room and Patio have front doors
        self.assertEqual(len(tiles_with_doors), 2)

        door_names = [tile.get_name() for tile in tiles_with_doors]
        self.assertIn("Dining Room", door_names)
        self.assertIn("Patio", door_names)

    def test_tiles_with_encounters(self):
        """Test tiles with encounters are correctly configured."""
        indoor = Tile.get_indoor_tiles()
        outdoor = Tile.get_outdoor_tiles()
        all_tiles = indoor + outdoor

        tiles_with_encounters = [
            tile for tile in all_tiles
            if tile.get_encounter() is not None
        ]
        # Kitchen, Storage, Evil Temple, Garden have encounters
        self.assertEqual(len(tiles_with_encounters), 4)


if __name__ == '__main__':
    # Run with: python -m unittest test.game_pieces.test_tile_creation
    # Or: python test_tile_creation.py (if in test/game_pieces/ directory)
    unittest.main(verbosity=2)
