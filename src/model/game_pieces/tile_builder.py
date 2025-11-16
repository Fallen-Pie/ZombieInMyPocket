from src.enums_and_types import *
from .tile import IndoorTile, OutdoorTile
from ..interfaces.i_tile import ITile
from ..encounters.not_implemented_encounters import IEncounter, TotemEncounter
from ..encounters.item_encounter import ItemEncounter
from ..encounters.health_encounter import HealthEncounter
from abc import ABC, abstractmethod

class TileBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_name(self, name) -> None:
        pass

    @abstractmethod
    def set_direction(self, direction) -> None:
        pass

    @abstractmethod
    def set_front_door(self, front_door) -> None:
        pass

    @abstractmethod
    def set_encounter(self, encounter) -> None:
        pass

class IndoorTileBuilder(TileBuilder):
    def __init__(self) -> None:
        self._tile = None
        self.reset()

    def reset(self) -> None:
        self._tile = IndoorTile()

    @property
    def product(self) -> ITile:
        tile = self._tile
        self.reset()
        return tile

    def set_name(self, name) -> None:
        self._tile.set_name(name)

    def set_direction(self, direction) -> None:
        self._tile.set_exists(direction)

    def set_front_door(self, front_door) -> None:
        self._tile.set_front_door(front_door)

    def set_encounter(self, encounter) -> None:
        self._tile.set_encounter(encounter)

class OutdoorTileBuilder(IndoorTileBuilder):
    def reset(self) -> None:
        self._tile = OutdoorTile()