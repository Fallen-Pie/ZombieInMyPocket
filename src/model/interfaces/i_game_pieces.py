from abc import ABC, abstractmethod
from .i_dev_card import IDevCard
from .i_tile import ITile
from ..game_time.game_time import ITime
from src.enums_and_types import *


class IGamePieces(ABC):

    @abstractmethod
    def setup(self, time: ITime) -> None:
        pass

    @abstractmethod
    def draw_dev_card(self) -> IDevCard:
        pass

    @abstractmethod
    def dev_cards_remaining(self) -> int:
        pass

    @abstractmethod
    def draw_indoor_tile(self) -> ITile:
        pass

    @abstractmethod
    def indoor_tiles_remaining(self) -> int:
        pass

    @abstractmethod
    def draw_outdoor_tile(self) -> ITile:
        pass

    @abstractmethod
    def outdoor_tiles_remaining(self) -> int:
        pass

    @abstractmethod
    def can_place_tile(self, new_tile: ITile, new_exit: Direction,
                       placed_tile: ITile,
                       placed_tile_exit: Direction) -> bool:
        pass

    @abstractmethod
    def place_tile(self, new_tile: ITile, new_exit: Direction,
                   placed_tile: ITile, placed_tile_exit: Direction) -> None:
        pass

    @abstractmethod
    def can_move_to_new_tile(self, placed_tile: ITile,
                             placed_tile_exit: Direction) -> bool:
        pass

    @abstractmethod
    def get_tile(self, position: Position) -> ITile | None:
        pass

    @abstractmethod
    def is_stuck(self) -> bool:
        pass

    @abstractmethod
    def get_tile_position(self, tile: ITile) -> Position:
        pass
