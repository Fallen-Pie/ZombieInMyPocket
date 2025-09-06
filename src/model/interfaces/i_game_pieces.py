"""Interface definition for game pieces management in Zombie in My Pocket.

This module defines the abstract base class for managing the physical game
components including development cards, tiles, and board placement logic.
"""

from abc import ABC, abstractmethod
from .i_dev_card import IDevCard
from .i_tile import ITile
from ..game_time.game_time import ITime
from src.enums_and_types import *


class IGamePieces(ABC):
    """Abstract interface for managing game pieces and board state.
    
    Handles the deck management, tile drawing, placement validation,
    and board state tracking for the game.
    """

    @abstractmethod
    def setup(self, time: ITime) -> None:
        """Initialize the game pieces including shuffling decks.
        
        Args:
            time: The game time manager
        """
        pass

    @abstractmethod
    def draw_dev_card(self) -> IDevCard:
        """Draw the next development card from the deck.
        
        Returns:
            The next development card to be used
        """
        pass

    @abstractmethod
    def dev_cards_remaining(self) -> int:
        """Get the number of development cards left in the deck.
        
        Returns:
            Number of cards remaining
        """
        pass

    @abstractmethod
    def draw_indoor_tile(self) -> ITile:
        """Draw the next indoor tile from the deck.
        
        Returns:
            The next indoor tile to be placed
        """
        pass

    @abstractmethod
    def indoor_tiles_remaining(self) -> int:
        """Get the number of indoor tiles left in the deck.
        
        Returns:
            Number of indoor tiles remaining
        """
        pass

    @abstractmethod
    def draw_outdoor_tile(self) -> ITile:
        """Draw the next outdoor tile from the deck.
        
        Returns:
            The next outdoor tile to be placed
        """
        pass

    @abstractmethod
    def outdoor_tiles_remaining(self) -> int:
        """Get the number of outdoor tiles left in the deck.
        
        Returns:
            Number of outdoor tiles remaining
        """
        pass

    @abstractmethod
    def can_place_tile(self, new_tile: ITile, new_exit: Direction,
                       placed_tile: ITile,
                       placed_tile_exit: Direction) -> bool:
        """Check if a new tile can be placed adjacent to an existing tile.
        
        Args:
            new_tile: The tile to be placed
            new_exit: The exit direction on the new tile
            placed_tile: The existing tile to connect to
            placed_tile_exit: The exit direction on the existing tile
            
        Returns:
            True if the placement is valid, False otherwise
        """
        pass

    @abstractmethod
    def place_tile(self, new_tile: ITile, new_exit: Direction,
                   placed_tile: ITile, placed_tile_exit: Direction) -> None:
        """Place a new tile adjacent to an existing tile on the board.
        
        Args:
            new_tile: The tile to place
            new_exit: The exit direction on the new tile
            placed_tile: The existing tile to connect to
            placed_tile_exit: The exit direction on the existing tile
        """
        pass

    @abstractmethod
    def can_move_to_new_tile(self, placed_tile: ITile,
                             placed_tile_exit: Direction) -> bool:
        """Check if the player can move to a tile through the given exit.
        
        Args:
            placed_tile: The tile to move from
            placed_tile_exit: The exit direction to use
            
        Returns:
            True if movement is possible, False otherwise
        """
        pass

    @abstractmethod
    def get_tile(self, position: Position) -> ITile | None:
        """Get the tile at a specific position on the board.
        
        Args:
            position: The board position to check
            
        Returns:
            The tile at that position, or None if no tile is placed there
        """
        pass

    @abstractmethod
    def is_stuck(self) -> bool:
        """Check if the player is unable to move due to lack of available tiles.
        
        Returns:
            True if the player cannot move and no tiles can be drawn
        """
        pass

    @abstractmethod
    def get_tile_position(self, tile: ITile) -> Position:
        """Get the board position of a specific tile.
        
        Args:
            tile: The tile to locate
            
        Returns:
            The position of the tile on the board
        """
        pass
