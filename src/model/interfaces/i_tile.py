from abc import ABC, abstractmethod
from src.enums_and_types import *
from ..encounters.encounters import IEncounter


class ITile(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def is_outdoors(self) -> bool:
        pass

    @abstractmethod
    def get_exits(self) -> tuple[Direction, ...]:
        """Given a rotation returns a list of exit directions"""

        pass

    @abstractmethod
    def get_front_door(self) -> Direction | None:
        """Given a rotation returns the direction to the front door
        or returns None if this tile is not the patio or dining room
        """

        pass

    @abstractmethod
    def get_encounter(self) -> IEncounter | None:
        """Gets the encounter for this tile if there is any otherwise
        returns None
        """

        pass

    @abstractmethod
    def set_rotation(self, rotation: Rotation) -> None:
        pass
