from unittest import TestCase

from HackerRank.dynamic_programming.grid_walking import GridWaling


class GridWalkingTest(TestCase):
    def setUp(self) -> None:
        self.instance = GridWaling()

    def test_walk_grid(self):
        n = 2
        m = 3
        x = [1, 1]
        grid = [2, 3]
        self.assertEqual(12, self.instance.count_all_possible_ways(n, m, grid, x))
