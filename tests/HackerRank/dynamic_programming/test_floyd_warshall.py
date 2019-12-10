from logging import getLogger
from os.path import realpath, dirname, join
from time import time
from typing import List
from unittest import TestCase

from HackerRank.dynamic_programming.floyd_warshall import Floyd


class FloydWarshallTest(TestCase):
    def setUp(self) -> None:
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')
        self.resources_dir = join(realpath(dirname(dirname(dirname(__file__)))), 'resources')

        n = 4
        edges = [[0, 5, None, 24], [None, 0, None, 6], [None, 7, 0, 4], [None, None, None, 0]]
        edges_to = [{0}, {0, 1, 2}, {2}, {0, 1, 2, 3}]
        self.flo = Floyd(edges, edges_to, n)

    def test_shortest_path(self):
        self.flo.shortest_distance_v2()
        q = 3
        from_to = [(1, 2), (3, 1), (1, 4)]
        for i in range(q):
            from_vertex, to_vertex = from_to[i]
            self.flo.shortest_distance_between(from_vertex - 1, to_vertex - 1) or -1

        start = time()

        results = []

        with open(join(self.resources_dir, 'floydWarshallInput.txt')) as f:
            n, m = map(int, f.readline().split())
            # edges = [[None]*n]*n is slower
            edges: List[List[int]] = [[None for _ in range(n)] for _ in range(n)]
            edges_to = [{i} for i in range(n)]
            for _ in range(m):
                tail, head, weight = map(int, f.readline().split())
                edges[tail - 1][head - 1] = weight
                edges_to[head - 1].add(tail - 1)
            for i in range(n):
                edges[i][i] = 0

            flo = Floyd(edges, edges_to, n)
            flo.shortest_distance_v2()
            q = int(f.readline())
            for _ in range(q):
                from_vertex, to_vertex = map(int, f.readline().split())
                results.append(flo.shortest_distance_between(from_vertex - 1, to_vertex - 1) or -1)

        self.logger.info(f'Execution time(s): {time() - start}')

        with open(join(self.resources_dir, 'floydWarshallOutput.txt')) as f:
            success = True
            for i in range(len(results)):
                success &= int(f.readline()) == results[i]
            self.assertEqual(True, success)


