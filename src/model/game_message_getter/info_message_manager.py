# import self

from ..interfaces.i_game_message_getter import IGameMessageGetter
from ...enums_and_types.game_message import MessageType, GameInstruction
from src.model.player.player import Player
from src.model.game_pieces.tile import Tile
from src.model.game_time import GameTime
from enum import Enum

class InfoMessageManager:
    """
    Handles all key-driven information messages (Stats, Tooltips, Instructions)
    without controlling game flow. Purely reads from player and turn_manager state
    and posts messages through msg_handler.
    """
    def __init__(self, msg_handler: IGameMessageGetter, player: Player, tile: Tile, time: GameTime):
        self.msg_handler = msg_handler
        self.player = player
        self.room = tile
        self.time = time

    def show_stats(self):
        """Post player's current stats as STATUS messages on player prompt (key press)."""
        stats = [
            f"Health: {self.player.get_health}",
            f"Attack: {self.player.get_attack_power}",
            f"Room: {self.room.get_name}",
            f"Time: {self.time.get_current_time}"
        ]
        for stat in stats:
            # here we don’t need enum, just reuse STATUS type
            self.msg_handler.post_message(MessageType.STATUS, Enum("Raw", {"VAL": stat}).VAL)

    def show_instructions(self):
        """
        Posts event-driven instructions based on current room.
        Can be extended with mapping of room -> GameInstruction
        """
        room_instruction_map = {
            "Storage Room": GameInstruction.STORAGE_ROOM,
            "Graveyard": GameInstruction.GRAVEYARD,
            "Evil Temple": GameInstruction.EVIL_TEMPLE,
        }

        current_room = getattr(self.player, "room", None)
        instruction = room_instruction_map.get(current_room)
        if instruction:
            self.msg_handler.post_message(MessageType.INSTRUCTION, instruction)


    def show_tooltip(self):
        """
        Gives key-driven instruction about item(s) in player's possession: Item name and attack score
        """
        items = getattr(self.player, "items", [])
        for item in items:
            # Expect each item has 'name' and 'attack_score'
            tooltip_text = f"{item.name} → Attack: {getattr(item, 'attack_score', 0)}"
            self.msg_handler.post_message(MessageType.INSTRUCTION, Enum("Raw", {"VAL": tooltip_text}).VAL)