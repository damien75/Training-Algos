#source Hackerrank / Algorithms / Search / Connected Cell in a Grid

#input: 2D binary grid with

#goal: return size of largest region / island, where connected components can be horizontally,
#vertically or diagonally

#idea: do a DFS / BFS through graph to analyze size of the region, and store the best

class exploreIsland:
    def __init__(self , grid):
        self.grid = grid

    def getNeighbors(self , position):
        i , j = position
        neighbors = []
        if i > 0:
            if j > 0:
                neighbors.append((i - 1 , j - 1))
            if j < len(self.grid[0]) - 1:
                neighbors.append((i - 1 , j + 1))
            neighbors.append((i - 1 , j))
        if i < len(self.grid) - 1:
            if j > 0:
                neighbors.append((i + 1 , j - 1))
            if j < len(self.grid[0]) - 1:
                neighbors.append((i + 1 , j + 1))
            neighbors.append((i + 1 , j))
        if j > 0:
            neighbors.append((i , j - 1))
        if j < len(self.grid[0]) - 1:
            neighbors.append((i , j + 1))
        return neighbors

    def sizeOfIslandFrom(self , i , j):
        size = 0
        toVisit = set()
        toVisit.add((i , j))
        while len(toVisit) > 0:
            curr = toVisit.pop()
            size += 1
            self.visited[curr[0]][curr[1]] = True
            neighbors = self.getNeighbors(curr)
            for neighbor in neighbors:
                i , j = neighbor
                if not self.visited[i][j] and neighbor not in toVisit and self.grid[i][j]:
                    toVisit.add(neighbor)
        return size

    def sizeBiggestIsland(self):
        biggest = 0
        n = len(self.grid)
        m = len(self.grid[0])
        self.visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not self.visited[i][j] and self.grid[i][j]:
                        biggest = max(biggest , self.sizeOfIslandFrom(i , j))
        return biggest

#Read input from Hackerrank
"""m = input()
n = input()
grid = []
for _ in range(m):
    line = map(int , raw_input().split())
    grid.append(line)

gr = exploreIsland(grid)
print gr.sizeBiggestIsland()"""

#Custom Inputs
m = n = 4
grid = [[1 , 1 , 0 , 0] ,
[0 , 1,  1,  0] ,
[0 , 0 , 1 , 0] ,
[1 , 0 , 0 , 0]]

gr = exploreIsland(grid)
print gr.sizeBiggestIsland() == 5
