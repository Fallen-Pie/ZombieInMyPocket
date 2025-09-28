from functools import partial


class EventDrivenManager:
    """Base class for event-driven managers."""

    def __init__(self, msg_handler):
        self.msg_handler = msg_handler
        self._event_map = {}

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
