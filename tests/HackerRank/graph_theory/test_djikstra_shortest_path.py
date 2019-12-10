from unittest import TestCase

from HackerRank.graph_theory.djikstra_shortest_path import Djikstra


class DjikstraShortestPathTest(TestCase):
    def test_get_shortest_path(self):
        edges = {1: {2: 24, 3: 3}, 2: {1: 24}, 3: {1: 3, 4: 12}, 4: {1: 20, 3: 12}}
        start = 1
        self.assertEqual([24, 3, 15], Djikstra(edges).djikstra_with_heap(start))
