#input : 2D grid (size x . y) with 0 for empty space, 1 for point (m such points) and 2 for obstacle

#goal: Find the empty space that is minimal distance from EVERY point marked by 1

#idea: Do a BFS from every point marked by 1 to compute distance to every reachable empty space
#also compute the number of start points that could get there

#complexity: O(x.y.m) building array in worst case in time and O(x.y) in space

class Grid:
    def __init__(self , grid):
        self.grid = grid
        self.distance = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] #travel distance to this point for each start point
        self.reach = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] #nb of start points that could reach this point
        self.nbStartPoints = 0

    def getNeighbors(self , x , y , distance):
        neighbors = []
        if x > 0 and self.grid[x - 1][y] == 0:
            neighbors.append((x - 1 , y , distance))
        if x < len(self.grid) - 1 and self.grid[x + 1][y] == 0:
            neighbors.append((x + 1 , y , distance))
        if y > 0 and self.grid[x][y - 1] == 0:
            neighbors.append((x , y - 1 , distance))
        if y < len(self.grid[x]) - 1 and self.grid[x][y + 1] == 0:
            neighbors.append((x , y + 1 , distance))
        return neighbors

    def computeDistanceFrom(self , startX , startY):
        toVisit = self.getNeighbors(startX , startY , 1)
        visited = [[False for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        while len(toVisit) > 0:
            x , y , distance = toVisit.pop(0)
            if not visited[x][y]:
                visited[x][y] = True
                self.distance[x][y] += distance
                self.reach[x][y] += 1
                toVisit.extend(self.getNeighbors(x , y , distance + 1))

    def getBestStartingPoint(self):
        minTravel = -1
        bestSol = -1
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    self.nbStartPoints += 1
                    self.computeDistanceFrom(x , y)
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if self.reach[x][y] == self.nbStartPoints:
                    if minTravel < 0:
                        minTravel = self.distance[x][y]
                        bestSol = (x , y)
                    else:
                        if self.distance[x][y] < minTravel:
                            minTravel = self.distance[x][y]
                            bestSol = (x , y)
        return bestSol , minTravel

#Example:
#1 - 0 - 2 - 0 - 1
#|   |   |   |   |
#0 - 0 - 0 - 0 - 0
#|   |   |   |   |
#0 - 0 - 1 - 0 - 0
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#expected answer: point (1,2) with total travel distance of 7
g = Grid(grid)
print g.getBestStartingPoint()
