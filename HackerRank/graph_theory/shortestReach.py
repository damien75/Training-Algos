#source Hackerrank / Algorithms / Graph Theory / Breadth First Search: Shortest Reach

#input= undirected graph with edge cost = 6

#goal: compute the shortest path distance from the start vertex s to all other vertices

#idea: Use BFS to compute all the distances

def shortestPathDistance(edges , start):
    distance = [-1]*len(edges.keys())
    distance[start] = 0
    explored = set()
    explored.add(start)
    toExplore = [start]
    while len(toExplore) > 0:
        v = toExplore.pop(0)
        for u in edges[v]:
            if u not in explored:
                toExplore.append(u)
                explored.add(u)
                distance[u] = distance[v] + 6
    distance.pop(start)
    return distance

#Read input from Hackerrank
"""t = input()

for i in range(t):
    n , m = map(int , raw_input().split())
    edges = {j : [] for j in range(n)}
    for j in range(m):
        tail , head = map(int , raw_input().split())
        edges[tail - 1].append(head - 1)
        edges[head - 1].append(tail - 1)
    start = input() - 1
    for dis in shortestPathDistance(edges , start):
        print dis,
    print"""

#Custom Inputs
t = 2
n = 4
m = 2
edges = {0 : [1 , 2] , 1 : [0] , 2 : [0] , 4 : []}
start = 0
for dis in shortestPathDistance(edges , start):
    print dis,
print
n = 3
m = 1
edges = {0 : [] , 1 : [2] , 2 : [1]}
start = 2
for dis in shortestPathDistance(edges , start):
    print dis,
print
