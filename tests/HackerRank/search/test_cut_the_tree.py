from unittest import TestCase

from HackerRank.search.cut_the_tree import CutTheTreeIn2


class CutTheTreeTest(TestCase):
    def setUp(self) -> None:
        self.weights = [100, 200, 100, 500, 100, 600]
        self.tree = {0: [1], 1: [0, 2, 4], 2: [3], 3: [4], 4: [1, 3, 5], 5: [4]}
        self.instance = CutTheTreeIn2()

    def test_get_min_diff_cut(self):
        self.assertEqual(400, self.instance.min_diff_cut(self.tree, self.weights, 0))
