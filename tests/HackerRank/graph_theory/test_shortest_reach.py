from unittest import TestCase

from HackerRank.graph_theory.shortest_reach import ShortestReach


class ShortestReachTest(TestCase):
    def setUp(self) -> None:
        self.instance = ShortestReach()

    def test_get_shortest_path1(self):
        edges = {0: [1, 2], 1: [0], 2: [0], 4: []}
        start = 0
        self.assertEqual([6, 6, -1], self.instance.shortest_path_distance(edges, start))

    def test_get_shortest_path2(self):
        edges = {0: [], 1: [2], 2: [1]}
        start = 2
        self.assertEqual([-1, 6], self.instance.shortest_path_distance(edges, start))
