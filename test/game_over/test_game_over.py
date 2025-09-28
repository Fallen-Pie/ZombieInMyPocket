from unittest import TestCase
from src.model.interfaces import IGameOver
from src.model.game_over import GameOver
from src.enums_and_types import GameOverReason


class TestGameOver(TestCase):

    def setUp(self) -> None:
        self.game_over: IGameOver = GameOver()
        self.test_reason: GameOverReason | None = None
        self.test_reason_2: GameOverReason | None = None
        self.game_over.game_over_event += self.set_test_reason

    def set_test_reason(self, reason: GameOverReason) -> None:
        self.test_reason = reason

    def set_test_reason_2(self, reason: GameOverReason) -> None:
        self.test_reason_2 = reason

    def test_health_zero(self):
        self.game_over.health_is_zero()
        expected = GameOverReason.HEALTH
        actual = self.test_reason
        self.assertEqual(expected, actual)

    def test_time_up(self):
        self.game_over.time_is_up()
        expected = GameOverReason.OUT_OF_TIME
        actual = self.test_reason
        self.assertEqual(expected, actual)

    def test_totem_buried(self):
        self.game_over.totem_is_buried()
        expected = GameOverReason.BURIED_TOTEM
        actual = self.test_reason
        self.assertEqual(expected, actual)

    def test_multiple_subscribers_health(self):
        self.game_over.game_over_event += self.set_test_reason_2
        self.game_over.health_is_zero()
        expected = (GameOverReason.HEALTH, GameOverReason.HEALTH)
        actual = (self.test_reason, self.test_reason_2)
        self.assertEqual(expected, actual)

    def test_multiple_subscribers_time_up(self):
        self.game_over.game_over_event += self.set_test_reason_2
        self.game_over.time_is_up()
        expected = (GameOverReason.OUT_OF_TIME, GameOverReason.OUT_OF_TIME)
        actual = (self.test_reason, self.test_reason_2)
        self.assertEqual(expected, actual)

    def test_multiple_subscribers_totem_buried(self):
        self.game_over.game_over_event += self.set_test_reason_2
        self.game_over.totem_is_buried()
        expected = (GameOverReason.BURIED_TOTEM, GameOverReason.BURIED_TOTEM)
        actual = (self.test_reason, self.test_reason_2)
        self.assertEqual(expected, actual)
