from typing import List, Tuple


class ExploreIsland:
    """
    Source Hackerrank / Algorithms / Search / Connected Cell in a Grid

    Input: 2D binary grid with

    Goal: return size of largest region / island, where connected components can be horizontally,
    vertically or diagonally

    Idea: do a DFS / BFS through graph to analyze size of the region, and store the best
    """

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

    def get_neighbors(self, position: Tuple[int, int]):
        i, j = position
        neighbors = []
        if i > 0:
            if j > 0:
                neighbors.append((i - 1, j - 1))
            if j < len(self.grid[0]) - 1:
                neighbors.append((i - 1, j + 1))
            neighbors.append((i - 1, j))
        if i < len(self.grid) - 1:
            if j > 0:
                neighbors.append((i + 1, j - 1))
            if j < len(self.grid[0]) - 1:
                neighbors.append((i + 1, j + 1))
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < len(self.grid[0]) - 1:
            neighbors.append((i, j + 1))
        return neighbors

    def size_of_island_from(self, i, j):
        size = 0
        to_visit = set()
        to_visit.add((i, j))
        while len(to_visit) > 0:
            curr = to_visit.pop()
            size += 1
            self.visited[curr[0]][curr[1]] = True
            neighbors = self.get_neighbors(curr)
            for neighbor in neighbors:
                i, j = neighbor
                if not self.visited[i][j] and neighbor not in to_visit and self.grid[i][j]:
                    to_visit.add(neighbor)
        return size

    def size_biggest_island(self):
        biggest = 0
        for i in range(self.height):
            for j in range(self.width):
                if not self.visited[i][j] and self.grid[i][j]:
                    biggest = max(biggest, self.size_of_island_from(i, j))
        return biggest

    @staticmethod
    def read_and_print_from_hackerrank():
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        m = int(input())
        grid = []
        for _ in range(m):
            line = list(map(int, input().split()))
            grid.append(line)

        gr = ExploreIsland(grid)
        print(gr.size_biggest_island())
