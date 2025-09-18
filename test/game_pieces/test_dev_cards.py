from unittest import TestCase
from src.model.game_pieces import GamePieces
from src.model.game_time.game_time import GameTime


class TestDevCards(TestCase):

    def setUp(self) -> None:
        self.time = GameTime()
        self.game_pieces = GamePieces(self.time)

    def test_starts_with_nine_dev_cards(self):
        expected = 9
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

    def test_draw_dev_card_removes_from_deck(self):
        expected = 9
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

        self.game_pieces.draw_dev_card()
        expected = 8
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

    def test_draw_last_card_reshuffles_deck(self):
        for _ in range(9):
            self.game_pieces.draw_dev_card()

        expected = 0
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

        self.game_pieces.draw_dev_card()
        expected = 8
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

    def test_draw_last_card_increases_time(self):
        for _ in range(9):
            self.game_pieces.draw_dev_card()
        
        expected = '9:00pm'
        actual = self.time.get_current_time()
        self.assertEqual(expected, actual)

        self.game_pieces.draw_dev_card()
        expected = '10:00pm'
        actual = self.time.get_current_time()
        self.assertEqual(expected, actual)
