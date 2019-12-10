from typing import List, Dict


class ShortestReach(object):
    """
    Source Hackerrank / Algorithms / Graph Theory / Breadth First Search: Shortest Reach

    Input= undirected graph with edge cost = 6

    Goal: compute the shortest path distance from the start vertex s to all other vertices

    Idea: Use BFS to compute all the distances
    """
    @staticmethod
    def shortest_path_distance(edges: Dict[int, List[int]], start: int) -> List[int]:
        distance = [-1] * len(edges.keys())
        distance[start] = 0
        explored = set()
        explored.add(start)
        to_explore = [start]
        while len(to_explore) > 0:
            v = to_explore.pop(0)
            for u in edges[v]:
                if u not in explored:
                    to_explore.append(u)
                    explored.add(u)
                    distance[u] = distance[v] + 6
        distance.pop(start)
        return distance

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())

        for i in range(t):
            n, m = map(int, input().split())
            edges = {j: [] for j in range(n)}
            for j in range(m):
                tail, head = map(int, input().split())
                edges[tail - 1].append(head - 1)
                edges[head - 1].append(tail - 1)
            start = int(input()) - 1
            for dis in self.shortest_path_distance(edges, start):
                print(dis,)
