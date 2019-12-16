from typing import List, Tuple


class Grid:
    """
    Input: 2D grid (size x . y) with 0 for empty space, 1 for point (m such points) and 2 for obstacle

    Goal: Find the empty space that is minimal distance from EVERY point marked by 1

    Idea: Do a BFS from every point marked by 1 to compute distance to every reachable empty space
    also compute the number of start points that could get there

    complexity: O(x.y.m) building array in worst case in time and O(x.y) in space
    """

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.distance = [[0 for _ in range(len(grid[0]))] for _ in
                         range(len(grid))]  # travel distance to this point for each start point
        self.reach = [[0 for _ in range(len(grid[0]))] for _ in
                      range(len(grid))]  # nb of start points that could reach this point
        self.nbStartPoints = 0

    def get_neighbors(self, x: int, y: int, distance: int) -> List[Tuple[int, int, int]]:
        neighbors = []
        if x > 0 and self.grid[x - 1][y] == 0:
            neighbors.append((x - 1, y, distance))
        if x < len(self.grid) - 1 and self.grid[x + 1][y] == 0:
            neighbors.append((x + 1, y, distance))
        if y > 0 and self.grid[x][y - 1] == 0:
            neighbors.append((x, y - 1, distance))
        if y < len(self.grid[x]) - 1 and self.grid[x][y + 1] == 0:
            neighbors.append((x, y + 1, distance))
        return neighbors

    def compute_distance_from(self, start_x: int, start_y: int):
        to_visit = self.get_neighbors(start_x, start_y, 1)
        visited = [[False for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        while len(to_visit) > 0:
            x, y, distance = to_visit.pop(0)
            if not visited[x][y]:
                visited[x][y] = True
                self.distance[x][y] += distance
                self.reach[x][y] += 1
                to_visit.extend(self.get_neighbors(x, y, distance + 1))

    def get_best_starting_point(self) -> Tuple[Tuple[int, int], int]:
        min_travel = -1
        best_sol = -1
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y] == 1:
                    self.nbStartPoints += 1
                    self.compute_distance_from(x, y)
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.reach[x][y] == self.nbStartPoints:
                    if min_travel < 0:
                        min_travel = self.distance[x][y]
                        best_sol = (x, y)
                    else:
                        if self.distance[x][y] < min_travel:
                            min_travel = self.distance[x][y]
                            best_sol = (x, y)
        return best_sol, min_travel
