from unittest import TestCase

from LeetCode.smallest_rectangle_enclosing import Enclosing


class EnclosingTest(TestCase):
    def test_smallest_rectangle(self):
        grid = [
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0]
        ]
        start_point = (0, 2)
        e = Enclosing(grid)
        self.assertEqual(6, e.smallest_area(start_point))
