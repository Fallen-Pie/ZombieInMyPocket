from src.enums_and_types import *
from ..interfaces.i_tile import ITile
from ..encounters.not_implemented_encounters import IEncounter

class IndoorTile(ITile):
    def __init__(self):
        self._name = None
        self._exits = None
        self._front_door = None
        self._encounter = None
        self._rotation = None

    def set_name(self, name) -> None:
        self._name = name

    def set_exists(self, exists) -> None:
        self._exits = exists

    def set_front_door(self, front_door) -> None:
        self._front_door = front_door

    def set_encounter(self, encounter) -> None:
        self._encounter = encounter

    def get_name(self) -> str:
        return self._name

    def get_exits(self) -> tuple[Direction, ...]:
        return tuple(Direction(
            (x.value + self._rotation.value) % 4) for x in self._exits)

    def get_front_door(self) -> Direction | None:
        if self._front_door is None:
            return None
        else:
            return Direction(
                (self._front_door.value + self._rotation.value) % 4)

    def get_encounter(self) -> IEncounter | None:
        return self._encounter

    def set_rotation(self, rotation: Rotation) -> None:
        self._rotation = rotation

class OutdoorTile(IndoorTile):
    pass

    # @staticmethod
    # def get_indoor_tiles() -> list[ITile]:
    #     return [
    #
    #         Tile("Bathroom", False,
    #              (Direction.NORTH,),
    #              None, None),
    #
    #         Tile("Kitchen", False,
    #              (Direction.NORTH, Direction.EAST, Direction.WEST),
    #              None, HealthEncounter(1)),
    #
    #         Tile("Storage", False,
    #              (Direction.NORTH,),
    #              None, ItemEncounter(None)),
    #
    #         Tile("Evil Temple", False,
    #              (Direction.EAST, Direction.WEST),
    #              None, TotemEncounter(False)),
    #
    #         Tile("Family Room", False,
    #              (Direction.NORTH, Direction.EAST, Direction.WEST),
    #              None, None),
    #
    #         Tile("Dining Room", False,
    #              (Direction.NORTH, Direction.EAST,
    #               Direction.SOUTH, Direction.WEST),
    #              Direction.NORTH, None),
    #
    #         Tile("Bedroom", False,
    #              (Direction.NORTH, Direction.WEST),
    #              None, None),
    #
    #         Tile("Foyer", False,
    #              (Direction.NORTH,),
    #              None, None),
    #     ]
    #
    # @staticmethod
    # def get_outdoor_tiles() -> list[ITile]:
    #     return [
    #
    #         Tile("Garden", True,
    #              (Direction.EAST, Direction.SOUTH, Direction.WEST),
    #              None, HealthEncounter(1)),
    #
    #         Tile("Sitting Area", True,
    #              (Direction.EAST, Direction.SOUTH, Direction.WEST),
    #              None, None),
    #
    #         Tile("Yard", True,
    #              (Direction.EAST, Direction.SOUTH, Direction.WEST),
    #              None, None),
    #
    #         # TODO: Add graveyard event
    #         Tile("Graveyard", True,
    #              (Direction.EAST, Direction.SOUTH),
    #              None, None),
    #
    #         Tile("Garage", True,
    #              (Direction.SOUTH, Direction.WEST),
    #              None, None),
    #
    #         Tile("Patio", True,
    #              (Direction.NORTH, Direction.EAST, Direction.SOUTH),
    #              Direction.NORTH, None),
    #
    #         Tile("Yard", True,
    #              (Direction.EAST, Direction.SOUTH, Direction.WEST),
    #              None, None),
    #
    #         Tile("Yard", True,
    #              (Direction.EAST, Direction.SOUTH, Direction.WEST),
    #              None, None),
    #     ]
