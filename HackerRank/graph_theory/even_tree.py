from typing import List, Tuple, Union


class CutTree:
    """
    Source Hackerrank / Algorithms / Graph Theory / Even Tree

    Input: Tree

    Goal: cut the max number of edges st each subtree we get has an odd nb of vertices

    Idea: build tree and then go through tree to count nb of children
    """
    def __init__(self, edges: List[Tuple[int, int]], height: int, m: int):
        self.edges = edges
        self.height = height
        self.m = m
        self.tree: List[Union[int, List[int]]] = []

    def find_children(self, n: int) -> List[int]:
        children = []
        for x in range(self.m):
            if self.edges[x][1] == n:
                children.append(self.edges[x][0])
                childN = self.find_children(self.edges[x][0])
                for child in childN:
                    children.append(child)
        return children

    def generate_tree(self):
        for x in range(self.height):
            self.tree.append([x+1])
        for x in range(self.height):
            self.tree[x].append(self.find_children(x + 1))
        return self.tree

    def number_edges_to_remove(self) -> int:
        self.generate_tree()

        count = 0
        for x in range(self.height):
            if len(self.tree[x][1]) % 2 == 1:
                count += 1
        return count - 1

    @staticmethod
    def read_and_print_from_hackerrank():
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        N, M = map(int, input().split())
        edges = []
        for x in range(M):
            u, v = map(int, input().split())
            edges.append((u, v))
        print(CutTree(edges, N, M).number_edges_to_remove())
