from unittest import TestCase

from LeetCode.shortest_distance_in_grid import Grid


class ShortestDistanceInGridTest(TestCase):
    def test_shortest_distance_from_points(self):
        """
        1 - 0 - 2 - 0 - 1
        |   |   |   |   |
        0 - 0 - 0 - 0 - 0
        |   |   |   |   |
        0 - 0 - 1 - 0 - 0

        expected answer: point (1,2) with total travel distance of 7
        """
        grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        g = Grid(grid)
        self.assertEqual(((1, 2), 7), g.get_best_starting_point())
