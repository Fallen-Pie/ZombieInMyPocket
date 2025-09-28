from ...enums_and_types.game_message import MessageType, EventMessage, AlertMessage
from ..interfaces.i_game_message_getter import IGameMessageGetter
from src.model.game_message_getter import  EventDrivenManager

class GameAlertManager(EventDrivenManager):
    """ Event-driven handling of alerts and invalid moves."""
    def __init__(self, msg_handler: IGameMessageGetter, player):
        # self.msg_handler = msg_handler
        super().__init__(msg_handler)
        self.player = player

    def check_low_health(self):
        if self.player.health <= 2:
            self.register_event(
                "low_health",
                lambda e: self.msg_handler.post_message(MessageType.ALERT,
                AlertMessage.LOW_HEALTH_WARNING)
            )
            # self.msg_handler.post_message(
            #     MessageType.ALERT,
            #     AlertMessage.LOW_HEALTH_WARNING
            # )

    def check_time_warning(self, time: int):
        if time == 11:  # 11PM
            self.register_event(
        "time_near_midnight",
                lambda e: self.msg_handler.post_message(
                    MessageType.ALERT,
                    AlertMessage.TIME_WARNING
                )
            )
            # self.msg_handler.post_message(
            #     MessageType.ALERT,
            #     AlertMessage.TIME_WARNING
            # )

    # def low_health(self):
    #     self.msg_handler.post_message(MessageType.ALERT, AlertMessage.LOW_HEALTH_WARNING)

    # def time_warning(self):
    #     self.msg_handler.post_message(MessageType.ALERT, AlertMessage.TIME_WARNING)

    def invalid_move(self, move_type: str):
        if move_type == "cower":
            self.register_event(
                "invalid_move",
                lambda e: self.msg_handler.post_message(
                    MessageType.ALERT,
                    AlertMessage.INVALID_COWER_MOVE
                )
            )
            # self.msg_handler.post_message(MessageType.ALERT, AlertMessage.INVALID_COWER_MOVE)
        elif move_type == "door":
            self.register_event(
                "invalid_move",
                lambda e: self.msg_handler.post_message(
                    MessageType.ALERT,
                    AlertMessage.INVALID_DOOR_EXIT_SELECTED
                )
            )
            # self.msg_handler.post_message(MessageType.ALERT, AlertMessage.INVALID_DOOR_EXIT_SELECTED)
        elif move_type == "grass":
            self.register_event(
                "invalid_move",
                lambda e: self.msg_handler.post_message(
                    MessageType.ALERT,
                    AlertMessage.INVALID_GRASS_PATH_SELECTED
                )
            )
            # self.msg_handler.post_message(MessageType.ALERT, AlertMessage.INVALID_GRASS_PATH_SELECTED)

