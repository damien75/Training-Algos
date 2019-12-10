from unittest import TestCase

from HackerRank.graph_theory.even_tree import CutTree


class EvenTreeTest(TestCase):
    def test_get_nb_edges_to_remove(self):
        N = 10
        M = 9
        edges = [(2, 1),
                 (3, 1),
                 (4, 3),
                 (5, 2),
                 (6, 1),
                 (7, 2),
                 (8, 6),
                 (9, 8),
                 (10, 8)]

        cut = CutTree(edges, N, M)
        self.assertEqual(2, cut.number_edges_to_remove())
