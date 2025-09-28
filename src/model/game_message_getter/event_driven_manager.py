from functools import partial


class EventDrivenManager:
    """Base class for event-driven managers."""

    def __init__(self, msg_handler):
        self.msg_handler = msg_handler
        self._event_map = {}

    # def register_event(self, event_type: str, msg_type, msg_enum, args_fn=None):
    #     """
    #     Map an event_type to a message posting.
    #
    #     args_fn: Optional function(event) -> list of args for formatting
    #     """
    #     self._event_map[event_type] = (msg_type, msg_enum, args_fn)
    #
    # def handle_event(self, event: dict):
    #     event_type = event.get("type")
    #     if event_type not in self._event_map:
    #         return  # Unknown event, ignore
    #
    #     msg_type, msg_enum, args_fn = self._event_map[event_type]
    #
    #     # Prepare arguments
    #     args = args_fn(event) if args_fn else []
    #     self.msg_handler.post_message(msg_type, msg_enum, *args)


    def register_event(self, event_type: str, handler):
        """Map an event type to a handler function."""
        self._event_map[event_type] = handler

    def handle_event(self, event: dict):
        event_type = event.get("type")
        if event_type in self._event_map:
            self._event_map[event_type](event)
        else:
            # optional: log unknown event or ignore
            pass
