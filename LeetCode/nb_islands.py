from typing import List

from LeetCode.union_find import UnionFind


class LandsInGrid:
    """
    Input : 2D grid (size n . m) with 0 for water, 1 for land

    Goal: Find the number of islands at each step as we add lands k times

    Idea: use a union find structure to keep track of the nb of islands and connect them if necessary

    complexity: O(k log n.m) in time and O(n.m) in space
    Indeed, k operations on union find with n nodes has complexity of O(k log n)!!!
    """

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.uf = UnionFind(n * m, None)  # we will use a linear representation for indices (i,j)=>i*n+j

    def count_islands_after_adding_lands(self, positions: List[List[int]]) -> List[int]:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []
        for pos in positions:
            linear_pos = pos[0] * self.n + pos[1]
            self.uf.ids[linear_pos] = linear_pos
            self.uf.count += 1
            for d in dirs:
                x = pos[1] + d[1]
                y = pos[0] + d[0]
                neighbor = linear_pos + d[0] * self.n + d[1]
                if x < 0 or x >= self.n or y < 0 or y >= self.m or self.uf.ids[neighbor] is None:
                    continue  # in this case the neighbor is either not defined or it is not land
                if self.uf.ids[neighbor] != self.uf.ids[linear_pos]:
                    self.uf.union(linear_pos, neighbor)
            result.append(self.uf.count)
        return result
