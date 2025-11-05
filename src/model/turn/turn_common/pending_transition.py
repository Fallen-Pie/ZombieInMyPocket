from typing import TypedDict, Callable, Any


class PendingTransition(TypedDict):
    """stores the state factory for a new state
    and any results from previous states to pass to it"""
    next_state: Callable[[], Any]
    previous_result: tuple[Any, ...] | None
