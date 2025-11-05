
from abc import ABC, abstractmethod
from typing import Callable

class IEvent[T](ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __iadd__(self, callback: Callable[[T], None]):
        pass

    @abstractmethod
    def __isub__(self, callback: Callable[[T], None]):
        pass

    @abstractmethod
    def __call__(self, arg: T) -> None:
        pass