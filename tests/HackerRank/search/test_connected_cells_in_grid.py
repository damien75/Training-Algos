from unittest import TestCase

from HackerRank.search.connected_cells_in_grid import ExploreIsland


class ConnectedCellsTest(TestCase):
    def setUp(self) -> None:
        grid = [[1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [1, 0, 0, 0]]

        self.instance = ExploreIsland(grid)

    def test_get_size_biggest_island(self):
        self.assertEqual(5, self.instance.size_biggest_island())
