"""Interface definitions for the Zombie in My Pocket game.

This module contains all the abstract base classes (interfaces) that define
the contracts for various game components including items, tiles, encounters,
players, and game management objects.
"""

from .i_item import IItem
from .i_dev_card import IDevCard
from .i_game_over import IGameOver
from .i_game_pieces import IGamePieces
from .i_tile import ITile
from .i_player import IPlayer
# 🔴 Added
from .i_encounter import IEncounter
from .i_turn import ITurn
from .i_game_message_manager import IGameMessageManager


__all__ = [
    'IItem',
    'IDevCard',
    'IGamePieces',
    'ITile',
    'IGameOver',
    'IPlayer',
# 🔴 Added
    'IEncounter',
    'ITurn',
    'IGameMessageManager'
]
