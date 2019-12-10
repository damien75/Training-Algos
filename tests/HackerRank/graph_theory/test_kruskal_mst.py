from unittest import TestCase

from HackerRank.graph_theory.kruskal_mst import MinimumSpanningTree


class MSTTest(TestCase):
    def setUp(self) -> None:
        self.instance = MinimumSpanningTree()

    def test_get_mst(self):
        edges = {0: [(1, 5), (2, 3), (3, 6)],
                 1: [(0, 5), (3, 7), (2, 4)],
                 2: [(0, 3), (1, 4), (3, 5)],
                 3: [(0, 6), (1, 7), (2, 5)]}

        self.assertEqual(12, self.instance.extract_mst(edges))
