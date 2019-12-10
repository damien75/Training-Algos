import sys
from typing import Tuple, List, Dict


class Heap:
    class HeapElement:
        def __init__(self, node: int, key: int):
            self.node = node
            self.key = key

    def __init__(self):
        self.h = []  # stores array with 1st element: best distance and 2nd element: node in graph
        self.ref = {}  # stores index in heap of a specific node

    def invariant(self, position: int):
        child1 = max(1, position*2)
        child2 = child1 + 1
        maxPosition = len(self.h) - 1
        if child1 > maxPosition:
            return True
        elif child2 > maxPosition:
            return self.h[position].key <= self.h[child1].key
        else:
            return self.h[position].key <= self.h[child1].key and self.h[position].key <= self.h[child2].key

    def swap(self, p1: int, p2: int):
        temp = self.h[p1]
        self.h[p1] = self.h[p2]
        self.h[p2] = temp
        tempRef = self.ref[self.h[p1].node]
        self.ref[self.h[p1].node] = self.ref[self.h[p2].node]
        self.ref[self.h[p2].node] = tempRef

    def bubble_up(self, position: int):
        parentPosition = position // 2
        while position > 0 and not self.invariant(parentPosition):
            self.swap(position , parentPosition)
            position = position // 2
            parentPosition = position // 2

    def sink_in(self, position: int):
        maxPosition = len(self.h) - 1
        while not self.invariant(position):
            child1 = max(1 , position*2)
            child2 = child1 + 1
            child1Key = self.h[child1].key
            if child2 <= maxPosition and child1Key > self.h[child2].key:
                self.swap(position , child2)
                position = child2
            else:
                self.swap(position , child1)
                position = child1

    def insert(self, node: int, key: int):
        self.h.append(self.HeapElement(node, key))
        self.ref[node] = len(self.h) - 1
        self.bubble_up(len(self.h) - 1)

    def delete(self, node: int):
        position = self.ref[node]
        maxPosition = len(self.h) - 1
        if position == maxPosition:
            node = self.h.pop().node
            self.ref.pop(node)
        else:
            self.swap(position , maxPosition)
            node = self.h.pop().node
            self.ref.pop(node)
            if self.invariant(position):
                self.bubble_up(position)
            else:
                self.sink_in(position)

    def update(self, node: int, key: int):
        self.delete(node)
        self.insert(node , key)

    def get_key(self, node: int) -> int:
        position = self.ref[node]
        return self.h[position].key

    def extract(self) -> HeapElement:
        extremum = self.h[0]
        self.swap(0 , len(self.h) - 1)
        node = self.h.pop().node
        self.ref.pop(node)
        self.sink_in(0)
        return extremum

class MinimumSpanningTree(object):
    """
    Source Hackerrank / Algorithms / Graph Theory / Kruskal (MST): Really Special Subtree

    Input: undirected graph with edges that have an integer cost

    Goal: compute the Minimum Spanning Tree (MST)

    Idea: We start to find out the MST by starting from a given (random) vertex
    Then, we want every time to pick the edge with minimum cost, this is why we use a heap:
    1)When we update the values in the heap, we want to make sure the the head is not already in the tree that we have,
    otherwise we will include loops further on.
    2)The heap is initialized with infinite cost for all edges, except for the edges connected to the starting vertex
    3)When we add a new vertex to the tree, we look at the other vertices this one is connected to:
    a)if the cost to one of this vertices is better than the one we had before adding this new vertex, we update it
    b)otherwise we don't change the heap
    We stop when our tree has reached the size of the graph, then we have the MST
    """
    def extract_mst(self, edges: Dict[int, List[Tuple[int, int]]]) -> int:
        X = set()
        s = list(edges.keys())[0]  # starting vertex chosen at random
        X.add(s)
        total_cost = 0
        heap = Heap()  # initialize heap with values for starting vertex s
        for u in edges.keys():
            if u != s:
                heap.insert(u, sys.maxsize)
        for v , cost in edges[s]:
            heap.update(v , cost)
        nb_vertices = len(edges.keys())
        while len(X) < nb_vertices:
            best_v = heap.extract()
            total_cost += best_v.key
            v = best_v.node
            for w , cost in edges[v]:
                if w not in X:
                    heap_value = heap.get_key(w)
                    if cost < heap_value:
                        heap.update(w, cost)
            X.add(v)
        return total_cost

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        n, m = map(int, input().split())
        edges = {i: [] for i in range(n)}
        for i in range(m):
            head, tail, cost = map(int, input().split())
            head -= 1
            tail -= 1
            edges[head].append((tail, cost))
            edges[tail].append((head, cost))

        print(self.extract_mst(edges))
