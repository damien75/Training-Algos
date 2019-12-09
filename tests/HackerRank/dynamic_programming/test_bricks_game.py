from unittest import TestCase

from HackerRank.dynamic_programming.bricks_game import MaxScore


class BricksGameTest(TestCase):
    def setUp(self) -> None:
        self.bricks_game_instance = MaxScore()

    def test_get_max_score(self):
        test_n = 5
        test_bricks = [999, 1, 1, 1, 0]
        self.assertEqual(self.bricks_game_instance.max_score(test_n, test_bricks), 1001)
        test_bricks_2 = [0, 1, 1, 1, 999]
        self.assertEqual(self.bricks_game_instance.max_score(test_n, test_bricks_2), 999)
