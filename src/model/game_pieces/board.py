from ..interfaces.i_tile import ITile
from src.enums_and_types import *

type TileDict = dict[Position, ITile]


class Board:

    def __init__(self) -> None:
        self._all_tiles: TileDict = {}

        # Keep track of the number of exits so we know if we
        # are stuck
        self._exits_available = 0

    def reset(self):
        self._all_tiles = {}

    def get_all_tiles(self) -> TileDict:
        return self._all_tiles

    def get_tile(self, position: Position) -> ITile | None:
        if position in self._all_tiles:
            return self._all_tiles[position]
        else:
            return None

    def place_tile(self, new_tile: ITile, new_exit: Direction,
                   placed_tile: ITile | None,
                   placed_tile_exit: Direction) -> None:
        new_tile.set_rotation(self.__get_rotation_to_align_door(
            new_exit, placed_tile_exit
        ))
        if placed_tile is None:
            pos = (0, 0)
        else:
            pos = self.get_tile_position(placed_tile)
            pos = self.__move_position(pos, placed_tile_exit)
        self._all_tiles[pos] = new_tile

        # Keep track of exits available
        self._exits_available += len(new_tile.get_exits())
        if len(self._all_tiles) > 1:
            self._exits_available -= 2

    def can_move_to_new_tile(self, placed_tile: ITile,
                             placed_tile_exit: Direction) -> bool:
        pos = self.get_tile_position(placed_tile)
        pos = self.__move_position(pos, placed_tile_exit)
        return pos not in self._all_tiles and \
            placed_tile_exit in placed_tile.get_exits()

    def can_place_tile(self, new_tile: ITile, new_exit: Direction,
                       placed_tile: ITile,
                       placed_tile_exit: Direction) -> bool:
        new_tile.set_rotation(self.__get_rotation_to_align_door(
            new_exit, placed_tile_exit
        ))
        result = self.__can_place_tile(new_tile, placed_tile,
                                       placed_tile_exit)
        new_tile.set_rotation(Rotation.NONE)
        return result

    def __can_place_tile(self, new_tile: ITile,
                         placed_tile: ITile,
                         placed_tile_exit: Direction) -> bool:
        if not self.can_move_to_new_tile(placed_tile, placed_tile_exit):
            return False

        reversed_dir = self.__reverse_direction(placed_tile_exit)

        # Handle indoor to outdoor
        if new_tile.is_outdoors() != placed_tile.is_outdoors():

            # Both tiles must have a front door
            if placed_tile.get_front_door() is None or \
                    new_tile.get_front_door() is None or \
                    placed_tile_exit != placed_tile.get_front_door() or \
                    new_tile.get_front_door() != reversed_dir:
                return False

        # Stop from placing an indoor tile after the front door
        if not placed_tile.is_outdoors() and \
                placed_tile.get_front_door() is not None and \
                placed_tile_exit is placed_tile.get_front_door() and \
                not new_tile.is_outdoors():
            return False

        # Make sure another door isn't facing a wall
        for dir in {Direction.NORTH, Direction.EAST,
                    Direction.SOUTH, Direction.WEST} - {reversed_dir}:
            pos = self.get_tile_position(placed_tile)
            pos = self.__move_position(pos, dir)
            if pos in self._all_tiles:
                exit_a = dir in new_tile.get_exits()
                exit_b = self.__reverse_direction(dir) in \
                    self._all_tiles[pos].get_exits()
                if exit_a != exit_b:
                    return False

                # if two doors match make sure it isn't going from
                # indoor to outdoor
                if exit_a and exit_b and new_tile.is_outdoors() != \
                        self._all_tiles[pos].is_outdoors():
                    return False

        # Nothing is stopping this tile from being placed
        return True

    def __get_rotation_to_align_door(self, new_exit: Direction,
                                     placed_tile_exit: Direction) -> Rotation:
        return Rotation((placed_tile_exit.value + 6 - new_exit.value) % 4)

    def get_tile_position(self, tile: ITile) -> Position:
        keys = self._all_tiles.keys()
        values = self._all_tiles.values()
        return (list(keys)[list(values).index(tile)])

    def is_stuck(self) -> bool:
        return self._exits_available <= 0

    def _direction_from_position(
            self,
            position_from: Position,
            position_to: Position) -> Direction | None:
        x = position_to[0] - position_from[0]
        y = position_to[1] - position_from[1]

        if x == 1 and y == 0:
            return Direction.EAST
        elif x == -1 and y == 0:
            return Direction.WEST
        elif x == 0 and y == 1:
            return Direction.NORTH
        elif x == 0 and y == -1:
            return Direction.SOUTH
        else:
            return None

    @staticmethod
    def __move_position(pos: Position, dir: Direction) -> Position:
        x, y = pos
        match dir:
            case Direction.NORTH:
                y += 1
            case Direction.EAST:
                x += 1
            case Direction.SOUTH:
                y -= 1
            case Direction.WEST:
                x -= 1
        return (x, y)

    @staticmethod
    def __reverse_direction(dir: Direction) -> Direction:
        return Direction((dir.value + 2) % 4)
