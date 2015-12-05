#source Hackerrank / Algorithms / Dynamic Programming / Floyd : City of Blinding Lights

#input: directed graph with n vertices and m weighted edges

#goal: compute shortest path between 2 nodes for q queries

#idea: HAVE A 2D array and not 3D!!!
#array A that keeps track of shortest length from i to j
#we will update this array by adding vertices 1 by 1
#At the beginning, A[i][j] = None if no edge i -> j, 0 if i == j , cost if there is an edge
#Then for k = 1..n, A[i][j] = min(A[i][j] , A[i][k] + A[k][j])

"""Tricks to improve python speed:
1) Use list of lists instead if dictionary.
2) Use None as infinity for 'early break'.
3) Use additional variables for inner lists to reduce the number of 'access by index' calls.
Something like this:
for v2 in vertices:
    tv2 = d[v2]
    for v1 in vertices:
        if d[v1][v2] is None: continue
        tv1= d[v1]
        for v3 in vertices:
            if tv2[v3] is None: continue
            ..."""

class Floyd:
    def __init__(self , graph):
        self.graph = graph

    def shortestDistance(self):
        n = len(self.graph)
        A = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            v1 = self.graph[i]
            A1 = A[i]
            for j in range(n):
                if i == j:
                    A1[j] = 0
                elif v1[j] is not None:
                    A1[j] = v1[j]
        for k in range(n):
            middle = A[k]
            for i in range(n):
                fromVertex = A[i]
                cost1 = fromVertex[k] #best cost to go from initial vertex to middle vertex
                if cost1 is None: #then impossible to go from vertex i to middle vertex k
                    continue
                for j in range(n):
                    cost3 = middle[j] #best cost to go from middle vertex to end vertex
                    if cost3 is None: #impossible to go from middle vertex to end vertex
                        continue
                    fromVertex[j] = min(fromVertex[j] , cost1 + cost3) or cost1 + cost3

        self.A = A

    def shortestDistanceBetween(self , fromVertex , toVertex):
        return self.A[fromVertex][toVertex]

#Read input from Hackerrank
"""n , m = map(int , raw_input().split())
edges = [[None for _ in range(n)] for _ in range(n)]
for _ in range(m):
    tail , head , weight = map(int , raw_input().split())
    edges[tail - 1][head - 1] = weight

flo = Floyd(edges)
flo.shortestDistance()
q = input()
for _ in range(q):
    fromVertex , toVertex = map(int , raw_input().split())
    print flo.shortestDistanceBetween(fromVertex - 1 , toVertex - 1) or -1
"""

#Custom Inputs
if __name__ == "__main__":
    import time

    n = 4
    m = 5
    edges = [[None , 5 , None , 24] , [None , None , None , 6] , [None , 7 , None , 4] , [None , None , None , None]]
    flo = Floyd(edges)
    flo.shortestDistance()
    q = 3
    fromTo = [(1 , 2) , (3 , 1) , (1 , 4)]
    for i in range(q):
        fromVertex , toVertex = fromTo[i]
        print flo.shortestDistanceBetween(fromVertex - 1 , toVertex - 1) or -1

    start = time.time()

    results = []

    with open('floydWarshallInput.txt') as f:
        n , m = map(int , f.readline().split())
        edges = [[None for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            tail , head , weight = map(int , f.readline().split())
            edges[tail - 1][head - 1] = weight

        flo = Floyd(edges)
        flo.shortestDistance()
        q = int(f.readline())
        for _ in range(q):
            fromVertex , toVertex = map(int , f.readline().split())
            results.append(flo.shortestDistanceBetween(fromVertex - 1 , toVertex - 1) or -1)

    print "Execution time:" , time.time() - start

    with open('floydWarshallOutput.txt') as f:
        success = True
        for i in range(len(results)):
            success &= int(f.readline()) == results[i]
        print success
