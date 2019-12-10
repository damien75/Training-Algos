from queue import PriorityQueue
from typing import Dict


class Djikstra:
    """
    Source Hackerrank / Algorithms / Graph Theory / Dijkstra: Shortest Reach 2

    Input: undirected graph with integer (positive) edge costs

    Goal: given a starting vertex, compute the shortest path to every other vertex, -1 if unreachable

    Idea: keep an hashtable A that gives the length of the shortest path to get from s to a given vertex v
    Use a PriorityQueue pq as a heap, where the min cost edge crossing the boundary between seen and not yet
    seen vertices
    while pq is not empty:
       use heap to get the shortest edge with tail seen and head outside of X
       A[head] = A[tail] + len(edge[tail -> head])
       updateEdgesCrossingBoundary
    """
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        self.graph = graph

    def update_edges_crossing_boundary(self, tail: int, shortest_path: Dict[int, int], pq: PriorityQueue):
        for head in self.graph[tail].keys():
            pq.put((shortest_path[tail] + self.graph[tail][head], head))

    def djikstra_with_heap(self, s: int):
        shortest_path_map = {s: 0}
        pq = PriorityQueue()
        self.update_edges_crossing_boundary(s, shortest_path_map, pq)
        while not pq.empty():
            cost, v = pq.get()
            if v in shortest_path_map:
                continue
            shortest_path_map[v] = cost
            self.update_edges_crossing_boundary(v, shortest_path_map, pq)
        for i in self.graph.keys():  # put -1 for unreachable vertices
            if i not in shortest_path_map:
                shortest_path_map[i] = -1
        shortest_path_map.pop(s)  # remove the start vertex from the hashtable
        return [shortest_path_map[v] for v in sorted(shortest_path_map.keys())]

    @staticmethod
    def read_and_print_from_hackerrank():
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())

        for i in range(t):
            n, m = map(int, input().split())
            edges = {}
            for j in range(m):
                tail, head, cost = map(int, input().split())
                if tail in edges:
                    if head in edges[tail]:
                        edges[tail][head] = min(edges[tail][head], cost)
                    else:
                        edges[tail][head] = cost
                else:
                    edges[tail] = {}
                    edges[tail][head] = cost
                if head in edges:
                    if tail in edges[head]:
                        edges[head][tail] = min(edges[head][tail], cost)
                    else:
                        edges[head][tail] = cost
                else:
                    edges[head] = {}
                    edges[head][tail] = cost
            start = int(input())

            djik = Djikstra(edges)

            for dis in djik.djikstra_with_heap(start):
                print(dis,)
