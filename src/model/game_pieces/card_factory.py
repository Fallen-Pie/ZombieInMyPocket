from typing import Self
from src.enums_and_types import CardType
from ..interfaces.i_card import ICard
from .dev_card import DevCard
from .tile import Tile


class CardFactory:

    # Singleton
    def __new__(cls) -> Self:
        if not hasattr(cls, "instance"):
            cls.instance = super(CardFactory, cls).__new__(cls)
        return cls.instance

    def get_cards(self, card_type: CardType) -> list[ICard]:

        # Create the dictionary of cards if it does not exist
        if not hasattr(self, "__cards"):
            self.__cards: dict[CardType, list[ICard]] = {}

        # Create the deck if it does not exist
        if card_type not in self.__cards:
            self.__cards[card_type] = self.__create_cards(card_type)

        # Shallow copy return the same cards every time
        return self.__cards[card_type].copy()

    @staticmethod
    def __create_cards(card_type: CardType) -> list[ICard]:
        match card_type:
            case CardType.DEVELOPMENT:
                return DevCard.get_dev_cards()
            case CardType.INDOOR_TILE:
                return Tile.get_indoor_tiles()
            case CardType.OUTDOOR_TILE:
                return Tile.get_outdoor_tiles()
