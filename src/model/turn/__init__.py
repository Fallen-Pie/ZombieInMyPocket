import os

from .turn import Turn

__all__ = [
    "Turn"
]

if os.getenv("RUNNING_TURN_TESTS") == "1":
    #running tests for the turn packages only
    #set environment variable to "RUNNING_TURN_TESTS=1"

    from .turn_flow import TurnFlow
    from .state import State
    from .turn_enums import Triggers, StateNames, ServiceNames, ServiceMethods

    __all__ = ["State",
               "TurnFlow",
               "Triggers",
               "StateNames",
               "ServiceNames",
               "ServiceMethods",

               ]