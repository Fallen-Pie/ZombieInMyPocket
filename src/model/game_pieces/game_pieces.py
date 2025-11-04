from random import shuffle

from src.common import IGamePieces, IDevCard, ITile, ITime, Direction, Position

from .tile import Tile
from .dev_card import DevCard
from .board import Board

class GamePieces(IGamePieces):

    def __init__(self, time: ITime) -> None:
        self._board = Board()
        self._dev_cards: list[IDevCard] = DevCard.get_dev_cards()
        self._indoor_tiles: list[ITile] = Tile.get_indoor_tiles()
        self._outdoor_tiles: list[ITile] = Tile.get_outdoor_tiles()
        self._time = time
        self.is_indoors = True

        # The top card before it is shuffled is the foyer
        # so add it to the board before we shuffle
        self._board.place_tile(self._indoor_tiles.pop(), Direction.NORTH,
                               None, Direction.SOUTH)

        # Shuffle the tiles
        shuffle(self._indoor_tiles)
        shuffle(self._outdoor_tiles)
        shuffle(self._dev_cards)

    def draw_dev_card(self) -> IDevCard:
        # Increase the time and reshuffle if no cards are left
        if self.dev_cards_remaining() == 0:
            self._time.increase_current_time()
            if self._time.get_current_time() != '12:00am':
                self._dev_cards = DevCard.get_dev_cards()
                shuffle(self._dev_cards)
        return self._dev_cards.pop()

    def dev_cards_remaining(self) -> int:
        return len(self._dev_cards)


    def draw_tile(self) -> ITile | None:
        the_tile = None
        if self.is_indoors and self._indoor_tiles_remaining() > 0:
            the_tile = self._draw_indoor_tile()
        elif not self.is_indoors and self._outdoor_tiles_remaining() > 0:
            the_tile = self._draw_outdoor_tile()
        return the_tile

    def _draw_indoor_tile(self) -> ITile:
        return self._indoor_tiles.pop()

    def _indoor_tiles_remaining(self) -> int:
        return len(self._indoor_tiles)

    def _draw_outdoor_tile(self) -> ITile:
        return self._outdoor_tiles.pop()

    def _outdoor_tiles_remaining(self) -> int:
        return len(self._outdoor_tiles)

    def _tiles_remaining(self) -> int:
        return self._indoor_tiles_remaining() + self._outdoor_tiles_remaining()

    def can_place_tile(self, new_tile: ITile, new_exit: Direction,
                       placed_tile: ITile,
                       placed_tile_exit: Direction) -> bool:
        return self._board.can_place_tile(new_tile, new_exit,
                                          placed_tile, placed_tile_exit)

    def can_move_to_new_tile(self, placed_tile: ITile,
                             placed_tile_exit: Direction) -> bool:

        # Can't move if there are no tiles left
        if self._outdoor_tiles_remaining() == 0:
            if placed_tile.is_outdoors():
                return False
            elif placed_tile.get_front_door() == placed_tile_exit:
                return False
        if self._indoor_tiles_remaining() == 0:
            if not placed_tile.is_outdoors():
                if placed_tile.get_front_door() != placed_tile_exit:
                    return False

        return self._board.can_move_to_new_tile(placed_tile, placed_tile_exit)

    def place_tile(self, new_tile: ITile, new_exit: Direction,
                   placed_tile: ITile, placed_tile_exit: Direction) -> None:
        if placed_tile.get_front_door() == placed_tile_exit:
            #moving outdoors or indoors
            self.is_indoors = not self.is_indoors
        self._board.place_tile(new_tile, new_exit, placed_tile,
                               placed_tile_exit)

    def get_tile(self, position: Position) -> ITile | None:
        return self._board.get_tile(position)

    def get_all_tiles(self):
        return self._board.get_all_tiles()

    def is_stuck(self) -> bool:
        return self._board.is_stuck() and self._tiles_remaining() > 0

    def get_tile_position(self, tile: ITile) -> Position:
        return self._board.get_tile_position(tile)
