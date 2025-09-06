from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from .turn_enums import Triggers, ServiceNames, ServiceMethods, StateNames

if TYPE_CHECKING:
    #only imported for type checking
    from .turn_flow import TurnFlow

class State(ABC):
    """The parent state class"""
    @abstractmethod
    def __init__(self, name: StateNames) -> None:
        self.name: StateNames = name
        self.result: tuple[Any, ...] | None = None
        self.trigger: Triggers | None = None
        self.context: TurnFlow | None = None #none should be assigned before exiting to help with clean up #TurnFlow
        self.needs_input: bool = False

    def use_service(self, service: ServiceNames, method: ServiceMethods, *args, **kwargs):
        """
        Calls a given method from a given service via the context
        Args:
            service: The service to call.
            method: The method to call.
            *args: Additional arguments passed to the method.
            **kwargs: Additional keyword arguments passed to the method.
            """
        return self.context.call_service_method(service, method, *args, **kwargs)

    def get_request_handler(self):
        """
        Gets the context request handler,
        only to be used as a callback passed to a service
         """
        return self.context.handle_request

    @abstractmethod
    def enter(self, *args, **kwargs) -> bool:
        """run when the state is entered
        Note, states should not call exit from with in enter (it makes a mess),
        set needs_input to Turn if handle_request will be called with a callback,
        else leave it as False
        """

    @abstractmethod
    def handle_request(self, *args, **kwargs):
        """handles incoming requests in a way that is unique to this state"""
        self.exit()

    @abstractmethod
    def exit(self):
        """sends trigger and results to context,
        removes context reference to help with clean up"""
        self.context.state_finished(self.trigger, self.result)
        self.context = None #set none to help with clean up
        #return quickly to give control back to context

