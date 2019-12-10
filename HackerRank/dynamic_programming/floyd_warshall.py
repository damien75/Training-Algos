from typing import List, Set


class Floyd:
    """
    Source Hackerrank / Algorithms / Dynamic Programming / Floyd : City of Blinding Lights

    Input: directed graph with n vertices and m weighted edges

    Goal: compute shortest path between 2 nodes for q queries

    Idea: HAVE A 2D array and not 3D!!!
    array A that keeps track of shortest length from i to j
    we will update this array by adding vertices 1 by 1
    At the beginning, A[i][j] = None if no edge i -> j, 0 if i == j , cost if there is an edge
    Then for k = 1..n, A[i][j] = min(A[i][j] , A[i][k] + A[k][j])
    """
    def __init__(self, graph: List[List[int]], edges_to: List[Set[int]], n: int):
        self.edges_to = edges_to
        self.graph = graph
        self.n = n

    def shortest_distance_v2(self) -> None:
        for k in range(self.n):
            middle = self.graph[k]
            for i in self.edges_to[k]:
                from_vertex = self.graph[i]
                cost1 = from_vertex[k]  # best cost to go from initial vertex to middle vertex
                for j in range(self.n):
                    if middle[j] is None:  # impossible to go from middle vertex to end vertex
                        continue
                    if from_vertex[j] is not None:
                        from_vertex[j] = min(from_vertex[j] , cost1 + middle[j])
                    else:
                        from_vertex[j] = cost1 + middle[j]
                        self.edges_to[j].add(i)

    def shortest_distance(self) -> None:
        for k in range(self.n):
            middle = self.graph[k]
            for i in range(self.n):
                if self.graph[i][k] is None:  # then impossible to go from vertex i to middle vertex k
                    continue
                from_vertex = self.graph[i]
                cost1 = from_vertex[k]  # best cost to go from initial vertex to middle vertex
                for j in range(self.n):
                    if middle[j] is None:  # impossible to go from middle vertex to end vertex
                        continue
                    from_vertex[j] = min(from_vertex[j] , cost1 + middle[j]) or cost1 + middle[j]

    def shortest_distance_between(self, from_vertex: int, to_vertex: int) -> int:
        return self.graph[from_vertex][to_vertex]
