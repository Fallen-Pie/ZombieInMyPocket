from abc import ABC, abstractmethod
from .i_dev_card import IDevCard
from .i_tile import ITile
from enums_and_types import *


class IGamePieces(ABC):

    @abstractmethod
    def setup(self) -> None:
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
    def can_place_tile(self, tile: ITile, tile_position: Position,
                       player_position: Position, rotation: Rotation) -> bool:
        pass

    @abstractmethod
    def place_tile(self, tile: ITile, position: Position,
                   rotation: Rotation) -> None:
        pass

    @abstractmethod
    def get_tile(self, position: Position) -> ITile:
        pass

    @abstractmethod
    def is_stuck(self) -> bool:
        pass

    @abstractmethod
    def does_tile_exist(self, position: Position) -> bool:
        pass
