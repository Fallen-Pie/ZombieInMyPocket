from ..interfaces.i_dev_card import IDevCard
from ..interfaces.i_game_pieces import IGamePieces
from ..interfaces.i_tile import ITile
from .tile import Tile
from .dev_card import DevCard
from .board import Board
from src.enums_and_types import *
from random import shuffle


class GamePieces(IGamePieces):

    def __init__(self) -> None:
        self.setup()

    def setup(self) -> None:
        self._board = Board()
        self._dev_cards: list[IDevCard] = DevCard.get_dev_cards()
        self._indoor_tiles: list[ITile] = Tile.get_indoor_tiles()
        self._outdoor_tiles: list[ITile] = Tile.get_outdoor_tiles()

        # The top card before it is shuffled is the foyer
        # so add it to the board before we shuffle
        self._board.place_tile(self._indoor_tiles.pop(), Direction.NORTH,
                               None, Direction.SOUTH)

        # Shuffle the tiles
        shuffle(self._indoor_tiles)
        shuffle(self._outdoor_tiles)

    def draw_dev_card(self) -> IDevCard:
        return self._dev_cards.pop()

    def dev_cards_remaining(self) -> int:
        return len(self._dev_cards)

    def draw_indoor_tile(self) -> ITile:
        return self._indoor_tiles.pop()

    def indoor_tiles_remaining(self) -> int:
        return len(self._indoor_tiles)

    def draw_outdoor_tile(self) -> ITile:
        return self._outdoor_tiles.pop()

    def outdoor_tiles_remaining(self) -> int:
        return len(self._outdoor_tiles)

    def tiles_remaining(self) -> int:
        return self.indoor_tiles_remaining() + self.outdoor_tiles_remaining()

    def can_place_tile(self, new_tile: ITile, new_exit: Direction,
                       placed_tile: ITile,
                       placed_tile_exit: Direction) -> bool:
        return self._board.can_place_tile(new_tile, new_exit,
                                          placed_tile, placed_tile_exit)

    def can_move_to_new_tile(self, placed_tile: ITile,
                             placed_tile_exit: Direction) -> bool:
        return self._board.can_move_to_new_tile(placed_tile, placed_tile_exit)

    def place_tile(self, new_tile: ITile, new_exit: Direction,
                   placed_tile: ITile, placed_tile_exit: Direction) -> None:
        self._board.place_tile(new_tile, new_exit, placed_tile,
                               placed_tile_exit)

    def get_tile(self, position: Position) -> ITile | None:
        return self._board.get_tile(position)

    def is_stuck(self) -> bool:
        return self._board.is_stuck() and self.tiles_remaining() > 0

    def get_tile_position(self, tile: ITile) -> Position:
        return self._board.get_tile_position(tile)
