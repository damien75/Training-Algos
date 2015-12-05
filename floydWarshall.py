#source Hackerrank / Algorithms / Dynamic Programming / Floyd : City of Blinding Lights

#input: directed graph with n vertices and m weighted edges

#goal: compute shortest path between 2 nodes for q queries

#idea

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

    def shortestDistance2(self):
        n = len(self.graph)
        A = [[[None for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            v1 = self.graph[i]
            A1 = A[i]
            for j in range(n):
                if i == j:
                    A1[j][0] = 0
                elif v1[j] is not None:
                    A1[j][0] = v1[j]

        for k in range(1 , n + 1):
            v1 = A[k - 1]
            for i in range(n):
                v2 = A[i]
                cost1 = v2[k - 1][k - 1]
                for j in range(n):
                    if v1[j][k - 1] is None or cost1 is None:
                        v2[j][k] = v2[j][k - 1]
                        continue
                    v3 = v2[j]
                    cost2 = v3[k - 1]
                    cost3 = v1[j][k - 1]
                    b1 = cost2 is not None
                    b2 = cost1 is not None and cost3 is not None
                    if b1 and b2:
                        v3[k] = min(cost2 , cost1 + cost3)
                    elif b2:
                        v3[k] = cost1 + cost3
        self.A = A

    def shortestDistance(self):
        """print '------------------------------------------'
        print '------------------------------------------'
        print '------------------------------------------'"""

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
        """print A
        print"""
        for k in range(n):
            middle = A[k]
            """print
            print 'k' , k , middle"""
            for i in range(n):
                fromVertex = A[i]
                """print
                print 'i' , i , fromVertex[k]"""
                """if fromVertex[k][k] is None: #then impossible to go from vertex i to middle vertex k
                    print 'none 1'
                    continue"""
                cost1 = fromVertex[k] #best cost to go from initial vertex to middle vertex
                if cost1 is None:
                    continue
                for j in range(n):
                    cost3 = middle[j] #best cost to go from middle vertex to end vertex
                    """print 'j' , j , middle[j]"""
                    if cost3 is None: #impossible to go from middle vertex to end vertex
                        """print 'none 2'"""
                        continue
                    cost2 = fromVertex[j] # best path cost from initial to end vertex so far without k
                    """print i , k , j , cost1 , cost3 , cost2"""
                    if cost2 is not None:
                        fromVertex[j] = min(cost2 , cost1 + cost3)
                    else:
                        fromVertex[j] = cost1 + cost3
                    """elif b1:
                        v3[k + 1:] = cost2"""
                    """print A"""

        #print len(A) , len(A[0]) , len(A[0][0])
        """print A"""
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
