#input : 2D grid (size n . m) with 0 for water, 1 for land

#goal: Find the number of islands at each step as we add lands k times

#idea: use a union find structure to keep track of the nb of islands and connect them if necessary

#complexity: O(k log n.m) in time and O(n.m) in space
#Indeed, k operations on union find with n nodes has complexity of O(k log n)!!!

from unionFind import UF

class isLandsInGrid:
    def __init__(self , n , m):
        self.n = n
        self.m = m
        self.uf = UF(n*m , None) #we will use a linear representation for indices (i,j)=>i*n+j

    def numIslandsAfterAddingLands(self , positions):
        dirs = [(-1 , 0) , (1 , 0) , (0 , -1) , (0 , 1)]
        result = []
        for pos in positions:
            linearPos = pos[0]*self.n + pos[1]
            self.uf.ids[linearPos] = linearPos
            self.uf.count += 1
            for d in dirs:
                x = pos[1] + d[1]
                y = pos[0] + d[0]
                neighbor = linearPos + d[0]*self.n + d[1]
                if x < 0 or x >= self.n or y < 0 or y >= self.m or self.uf.ids[neighbor] is None:
                    continue #in this case the neighbor is either not defined or it is not land
                if self.uf.ids[neighbor] != self.uf.ids[linearPos]:
                    self.uf.union(linearPos , neighbor)
            result.append(self.uf.count)
        return result

#Example:

m = 3
n = 3
positions = [[0,0], [0,1], [1,2], [2,1]]

#Initially
#0 0 0
#0 0 0
#0 0 0

#Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#1 0 0
#0 0 0   Number of islands = 1
#0 0 0

#Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#1 1 0
#0 0 0   Number of islands = 1
#0 0 0

#Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#1 1 0
#0 0 1   Number of islands = 2
#0 0 0

#Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#1 1 0
#0 0 1   Number of islands = 3
#0 1 0

expectedResult =  [1, 1, 2, 3]

i = isLandsInGrid(n , m)
print i.numIslandsAfterAddingLands(positions)
print "should be equal to " , expectedResult
