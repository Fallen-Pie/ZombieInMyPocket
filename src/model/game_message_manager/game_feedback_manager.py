from ...enums_and_types.game_message import MessageType, EventMessage, GameStateMessage, GameOverMessage
from ..interfaces.i_game_message_manager import IGameMessageGetter

class GameFeedbackManager:
    """Handles feedback-type messages, as a response to player's actions."""
    def __init__(self, msg_handler: IGameMessageGetter):
        self.msg_handler = msg_handler

    def on_game_state_change(self, desc: str):
        self.msg_handler.post_message(MessageType.FEEDBACK, EventMessage.GAME_STATE, desc)

    def on_time_change(self, new_time: int):
        self.msg_handler.post_message(
            MessageType.FEEDBACK,
            GameStateMessage.TIME_CHANGE,
            new_time
        )

    def on_room_change(self, room_name: str):
        self.msg_handler.post_message(
            MessageType.FEEDBACK,
            GameStateMessage.ROOM_CHANGED,
            room_name
        )

    def on_item_acquired(self, item: str):
        self.msg_handler.post_message(
            MessageType.FEEDBACK,
            GameStateMessage.ITEM_ACQUIRED,
            item
        )

    def on_game_over(self, game_over_msg: GameOverMessage):
        self.msg_handler.post_message()