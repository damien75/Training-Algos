#input : binary 2D grid of dimension n . m and location (i , j) of a value 1

#goal: Return the area of the smallest rectangle enclosing all 1 values
#we can assume there is only 1 region to enclose and that this region is connected (no gaps)

#idea: Since the region is connected, then:
#   if a column i has a value 1 and column i-1 has no value 1, then the left border is i
#   ==> therefore we will use a binary search starting from column i to find left and right border
#       and a binary search starting from line j to find top and bottom borders

#complexity: O(n log m + m log n) in time and O(1) in space

class Enclosing:
    def __init__(self , grid):
        self.grid = grid

    def containsValue(self , m , inRow):
        if inRow:
            return 1 in self.grid[m]
        else:
            return 1 in [self.grid[i][m] for i in range(len(self.grid))]

    def searchLeft(self , i , j):
        while i <= j:
            m = (i + j)/2
            if not self.containsValue(m , False): #check if this column has a 1 value
                i = m + 1 #in that case the area is further right
            else:
                j = m - 1
        return i

    def searchRight(self , i , j):
        while i <= j:
            m = (i + j)/2
            if not self.containsValue(m , False): #check if this column has a 1 value
                j = m - 1 #in that case the area is further left
            else:
                i = m + 1
        return j

    def searchTop(self , i , j):
        while i <= j:
            m = (i + j)/2
            if not self.containsValue(m , True): #check if this column has a 1 value
                i = m + 1 #in that case the area is further down
            else:
                j = m - 1
        return i

    def searchBottom(self , i , j):
        while i <= j:
            m = (i + j)/2
            if not self.containsValue(m , True): #check if this column has a 1 value
                j = m - 1 #in that case the area is further up
            else:
                i = m + 1
        return j

    def smallestArea(self , startPoint):
        i , j = startPoint
        left = self.searchLeft(0 , i)
        right = self.searchRight(i + 1 , len(self.grid[i]) - 1)
        top = self.searchTop(0 , j)
        bottom = self.searchBottom(j + 1 , len(self.grid) - 1)
        return (bottom - top + 1)*(right - left + 1)

#Example:
grid = [
  [0 , 0 , 1 , 0],
  [0 , 1 , 1 , 0],
  [0 , 1 , 0 , 0]
]
startPoint = (0 , 2)
e = Enclosing(grid)
print e.smallestArea(startPoint) , "should be equal to" , 6
