#source Hackerrank / Algorithms / Dynamic Programming / Coin on the Table

#input: grid of size n x m with instructions and a goal

#goal: reach the goal with time t <= k, changing as few instructions on grid as possible

#idea: see in the grid in how many moves t we can get to a given point, while t <= k
#case 1: we can reach the goal with t <= k --> output 0
#case 2: start from * and see in how many moves we can get to their neighbors,
#if for one of them we can get there with moves <

import sys

def nbChangesForSolution(grid , n , m , k , iDestination , jDestination):
    fromDir = [(0 , 1 , 'L'), (0 , -1 , 'R'), (-1 , 0 , 'D'), (1 , 0 , 'U')]
    f = [[[sys.maxint for _ in range(k + 1)] for _ in range(m)] for _ in range(n)] #f will count the modifications
    for i in range(k + 1):
        f[0][0][i] = 0      #0 steps needed to get there

    for l in range(1 , k + 1):
        for i in range(n):
            for j in range(m):
                #our current position
                for direction in fromDir:
                    #direction is where we can come from
                    iFrom = i + direction[0]
                    jFrom = j + direction[1]
                    if 0<=iFrom<n and 0<=jFrom<m:
                        if grid[iFrom][jFrom] == direction[2]: #if the direction was pointing to us, then pick the best
                            f[i][j][l] = min(f[i][j][l], f[iFrom][jFrom][l - 1]) #no modification in this case
                        else:
                            f[i][j][l] = min(f[i][j][l], f[iFrom][jFrom][l - 1] + 1) #modification so +1 here

    mini = sys.maxint

    for l in range(k + 1):
        mini = min(mini, f[iDestination][jDestination][l])
    return mini if mini!=sys.maxint else -1

#Read input from Hackerrank
"""n , m , k = map(int , raw_input().split())
grid = []
for i in range(n):
    line = list(raw_input())
    if '*' in line:
        iDestination = i
        jDestination = line.index('*')
    grid.append(line)
print nbChangesForSolution(grid , n  , m , k , iDestination , jDestination)
"""

#Custom Inputs
if __name__ == "__main__":
    n = m = 2
    K = 3
    grid = [["R" , "D"] , ["*" , "L"]]
    iDestination = 1
    jDestination = 0
    print nbChangesForSolution(grid , n  , m , K , iDestination , jDestination)
    K = 1
    print nbChangesForSolution(grid , n  , m , K , iDestination , jDestination)
