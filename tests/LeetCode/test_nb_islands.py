from unittest import TestCase

from LeetCode.nb_islands import LandsInGrid


class LandsInGridTest(TestCase):
    def setUp(self) -> None:
        m = 3
        n = 3
        self.instance = LandsInGrid(n, m)

    def test_count_islands(self):
        """
        Initially
        0 0 0
        0 0 0
        0 0 0

        Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
        1 0 0
        0 0 0   Number of islands = 1
        0 0 0

        Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
        1 1 0
        0 0 0   Number of islands = 1
        0 0 0

        Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
        1 1 0
        0 0 1   Number of islands = 2
        0 0 0

        Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
        1 1 0
        0 0 1   Number of islands = 3
        0 1 0
        """
        positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
        self.assertListEqual([1, 1, 2, 3], self.instance.count_islands_after_adding_lands(positions))
