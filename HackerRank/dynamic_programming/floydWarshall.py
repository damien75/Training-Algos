#source Hackerrank / Algorithms / Dynamic Programming / Floyd : City of Blinding Lights

#input: directed graph with n vertices and m weighted edges

#goal: compute shortest path between 2 nodes for q queries

#idea: HAVE A 2D array and not 3D!!!
#array A that keeps track of shortest length from i to j
#we will update this array by adding vertices 1 by 1
#At the beginning, A[i][j] = None if no edge i -> j, 0 if i == j , cost if there is an edge
#Then for k = 1..n, A[i][j] = min(A[i][j] , A[i][k] + A[k][j])

class Floyd:
    def __init__(self , graph , edgesTo , n):
        self.edgesTo = edgesTo
        self.graph = graph
        self.n = n

    def shortestDistance2(self):
        for k in range(self.n):
            middle = self.graph[k]
            for i in self.edgesTo[k]:
                fromVertex = self.graph[i]
                cost1 = fromVertex[k] #best cost to go from initial vertex to middle vertex
                for j in range(self.n):
                    if middle[j] is None: #impossible to go from middle vertex to end vertex
                        continue
                    if fromVertex[j] is not None:
                        fromVertex[j] = min(fromVertex[j] , cost1 + middle[j])
                    else:
                        fromVertex[j] = cost1 + middle[j]
                        self.edgesTo[j].add(i)

    def shortestDistance(self):
        for k in range(self.n):
            middle = self.graph[k]
            for i in range(self.n):
                if self.graph[i][k] is None: #then impossible to go from vertex i to middle vertex k
                    continue
                fromVertex = self.graph[i]
                cost1 = fromVertex[k] #best cost to go from initial vertex to middle vertex
                for j in range(self.n):
                    if middle[j] is None: #impossible to go from middle vertex to end vertex
                        continue
                    fromVertex[j] = min(fromVertex[j] , cost1 + middle[j]) or cost1 + middle[j]

    def shortestDistanceBetween(self , fromVertex , toVertex):
        return self.graph[fromVertex][toVertex]

#Read input from Hackerrank
"""n , m = map(int , raw_input().split())
edges = [[None for _ in range(n)] for _ in range(n)]
for _ in range(m):
    tail , head , weight = map(int , raw_input().split())
    edges[tail - 1][head - 1] = weight

flo = Floyd(edges , n)
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
    edges = [[0 , 5 , None , 24] , [None , 0 , None , 6] , [None , 7 , 0 , 4] , [None , None , None , 0]]
    edgesTo = [set([0]) , set([0 , 1 , 2]) , set([2]) , set([0 , 1 , 2 , 3])]
    flo = Floyd(edges , edgesTo , n)
    flo.shortestDistance2()
    q = 3
    fromTo = [(1 , 2) , (3 , 1) , (1 , 4)]
    for i in range(q):
        fromVertex , toVertex = fromTo[i]
        print flo.shortestDistanceBetween(fromVertex - 1 , toVertex - 1) or -1

    start = time.time()

    results = []

    with open('floydWarshallInput.txt') as f:
        n , m = map(int , f.readline().split())
        #edges = [[None]*n]*n is slower
        edges = [[None for _ in range(n)] for _ in range(n)]
        edgesTo = [set([i]) for i in range(n)]
        for _ in range(m):
            tail , head , weight = map(int , f.readline().split())
            edges[tail - 1][head - 1] = weight
            edgesTo[head - 1].add(tail - 1)
        for i in range(n):
            edges[i][i] = 0

        flo = Floyd(edges , edgesTo , n)
        flo.shortestDistance2()
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
