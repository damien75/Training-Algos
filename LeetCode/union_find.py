from typing import Any


class UnionFind:
    """
    Input : number of nodes n and list of undirected edges

    Goal: Find the number of connected components in the graph

    Idea: Use a union find data structure and then output the number of connected components

    complexity: O(n^2) building data structure in worst case in time and O(n) in space
    """

    def __init__(self, n: int, default_value: Any = False):
        if default_value is not False:
            self.ids = [default_value for _ in range(n)]
            self.count = 0
        else:
            self.ids = [i for i in range(n)]
            self.count = n

    def union(self, id1: Any, id2: Any):
        i1 = self.ids[id1]
        i2 = self.ids[id2]
        if i1 != i2:
            for i in range(len(self.ids)):
                if self.ids[i] == i2:
                    self.ids[i] = i1
            self.count -= 1

    def is_connected(self, id1: Any, id2: Any):
        return self.ids[id1] == self.ids[id2]
