from unittest import TestCase

from HackerRank.dynamic_programming.coin_on_the_table import CoinOnTheTable


class CoinOnTheTableTest(TestCase):
    def setUp(self) -> None:
        self.instance = CoinOnTheTable()

    def test_nb_ways_to_change_for_amount(self):
        n = m = 2
        k = 3
        grid = [["R", "D"], ["*", "L"]]
        i_destination = 1
        j_destination = 0
        self.assertEqual(0, self.instance.nb_changes_for_solution(grid, n, m, k, i_destination, j_destination))
        k = 1
        self.assertEqual(1, self.instance.nb_changes_for_solution(grid, n, m, k, i_destination, j_destination))
