"""Interface definitions for the Zombie in My Pocket game.

This module contains all the abstract base classes (interfaces) that define
the contracts for various game components including items, tiles, encounters,
players, and game management objects.
"""

from .i_dev_card import IDevCard
from .i_encounter import IEncounter
from .i_game_pieces import IGamePieces
from .i_item import IItem
from .i_player import IPlayer
from .i_tile import ITile
from .i_game_over import IGameOver
from .i_time import ITime
from .i_turn import ITurn
from .i_game_status import IGameStatus
from .i_event import IEvent

__all__ = [
    'IDevCard',
    'IEncounter',
    'IGamePieces',
    'IItem',
    'IPlayer',
    'ITile',
    'IGameOver',
    'ITurn',
    'ITime',
    'IGameStatus',
    'IEvent',
]
