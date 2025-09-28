from ...enums_and_types.game_message import MessageType, GameFeedbackMessage, GameOverMessage
from ..interfaces.i_game_message_manager import IGameMessageManager


class GameFeedbackManager:
    """Handles feedback-type messages, as a response to player's actions."""
    def __init__(self, msg_handler: IGameMessageManager):
        self.msg_handler = msg_handler

    def on_game_state_change(self, desc: str):
        self.msg_handler.post_message(MessageType.FEEDBACK, MessageType.STATUS, desc)

    def on_time_change(self, new_time: int):
        self.msg_handler.post_message(
            MessageType.FEEDBACK,
            GameFeedbackMessage.TIME_CHANGE,
            new_time
        )

    def on_room_change(self, room_name: str):
        self.msg_handler.post_message(
            MessageType.FEEDBACK,
            GameFeedbackMessage.ROOM_CHANGED,
            room_name
        )

    def on_item_acquired(self, item: str):
        self.msg_handler.post_message(
            MessageType.FEEDBACK,
            GameFeedbackMessage.ITEM_ACQUIRED,
            item
        )

    def on_game_over(self, game_over_msg: GameOverMessage):
        self.msg_handler.post_message(game_over_msg)