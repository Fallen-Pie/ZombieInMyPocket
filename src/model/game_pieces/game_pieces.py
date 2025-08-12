from ..interfaces.i_dev_card import IDevCard
from ..interfaces.i_game_pieces import IGamePieces
from ..interfaces.i_tile import ITile
from .tile import Tile
from .board import Board
from enums_and_types import *
from random import shuffle


class GamePieces(IGamePieces):

    def __init__(self) -> None:
        self.setup()

    def setup(self) -> None:
        self._board = Board()
        self._dev_cards: list[IDevCard] = []
        self._indoor_tiles: list[ITile] = Tile.get_indoor_tiles()
        self._outdoor_tiles: list[ITile] = Tile.get_outdoor_tiles()

        # The top card before it is shuffled is the foyer
        # so add it to the board before we shuffle
        self._board.place_tile(self._indoor_tiles.pop(), (0, 0), Rotation.NONE)

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

    def can_place_tile(self, tile: ITile, tile_position: Position,
                       player_position: Position, rotation: Rotation) -> bool:
        return self._board.can_place_tile(
            tile, tile_position, player_position, rotation)

    def place_tile(self, tile: ITile, position: Position,
                   rotation: Rotation) -> None:
        self._board.place_tile(tile, position, rotation)

    def get_tile(self, position: Position) -> ITile:
        return self._board.get_tile(position)

    def is_stuck(self) -> bool:
        return self._board.is_stuck()

    def does_tile_exist(self, position: Position) -> bool:
        pass
