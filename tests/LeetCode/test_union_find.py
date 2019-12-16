from unittest import TestCase

from LeetCode.union_find import UnionFind


class UnionFindTest(TestCase):
    def test_union_count_1(self):
        """
        0          3
        |          |
        1 --- 2    4

        expect to return 2.
        """
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])
        self.assertEqual(2, uf.count)

    def test_union_count_2(self):
        """
        0           4
        |           |
        1 --- 2 --- 3

        expect to return 1.
        """
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])
        self.assertEqual(1, uf.count)
