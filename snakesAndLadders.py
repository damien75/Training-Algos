#source Hackerrank / Algorithms / Search / Snakes And Ladders

#input: array of shortcuts (ladders to go up faster and snakes to go back down)

#goal: find fastest way to get to the top, where we can roll a dice every time

#idea: store jumps in array, if no snake or ladder at this position then jumps[i] = i
#then use a heap sorted using the number of tosses used to get there
#keep track of the positions already explored and stop when we've reached the top or run out of tries

import heapq , time

def minNumberToss(jumps , top):
    nbToss = 0

    positions = [(0 , 1)]
    explored = [False for i in range(top + 7)]

    while len(positions) > 0:
        nbToss , p = heapq.heappop(positions)
        while explored[p]:
            if len(positions) <= 0:
                return -1
            nbToss , p = heapq.heappop(positions)
        explored[p] = True
        if p == top:
            return nbToss
        elif p < top:
            for i in range(1 , 7):
                heapq.heappush(positions , (nbToss + 1 , jumps[p + i]))
    return -1

#Read input from Hackerrank
top = 100
"""t = input()
for _ in range(t):
    n = input()
    jumps = [i for i in range(top + 8)]
    for l in range(n):
        s , e = map(int , raw_input().split())
        jumps[s] = e
    m = input()
    for l in range(m):
        s , e = map(int , raw_input().split())
        jumps[s] = e
    print minNumberToss(jumps , top)"""

#Custom Inputs
start = time.time()

results = []

with open('snakesInput2.txt') as f:
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        jumps = [i for i in range(top + 8)]
        for l in range(n):
            s , e = map(int , f.readline().split())
            jumps[s] = e
        m = int(f.readline())
        for l in range(m):
            s , e = map(int , f.readline().split())
            jumps[s] = e
        results.append(minNumberToss(jumps , top))

print "Execution time:" , time.time() - start
print results
with open('snakesOutput2.txt') as f:
    success = True
    for i in range(len(results)):
        success &= int(f.readline()) == results[i]
    print success
