from typing import TypeVar, Callable
from src.common import IEvent

T = TypeVar('T')

class Event(IEvent[T]):

    def __init__(self) -> None:
        self.__subscribers: set[Callable[[T], None]] = set()

    def __iadd__(self, callback: Callable[[T], None]):
        self.__subscribers.add(callback)
        return self

    def __isub__(self, callback: Callable[[T], None]):
        self.__subscribers.remove(callback)
        return self

    def __call__(self, arg: T) -> None:
        for subscriber in self.__subscribers:
            subscriber(arg)
