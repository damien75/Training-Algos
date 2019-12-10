from unittest import TestCase

from HackerRank.dynamic_programming.coin_change import CoinChange


class CoinChangeTest(TestCase):
    def setUp(self) -> None:
        self.instance = CoinChange()

    def test_nb_ways_to_change_for_amount(self):
        self.assertEqual(4, self.instance.nb_ways(4, 3, [1, 2, 3]))
        self.assertEqual(5, self.instance.nb_ways(10, 4, [2, 5, 3, 6]))
