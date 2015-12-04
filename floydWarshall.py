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

    def shortestDistance(self):
        n = len(self.graph.keys())
        A = [[[None for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]
        for i in range(1 , n + 1):
            v1 = self.graph[i]
            A1 = A[i - 1]
            for j in range(1 , n + 1):
                if i == j:
                    A1[j - 1][0] = 0
                elif v1[j] != None:
                    A1[j - 1][0] = v1[j]

        for k in range(1 , n + 1):
            v1 = A[k - 1]
            for i in range(1 , n + 1):
                v2 = A[i - 1]
                if v2[k - 1] == None:
                    continue
                cost1 = v2[k - 1][k - 1]
                for j in range(1 , n + 1):
                    if v1[j - 1] == None:
                        continue
                    v3 = v2[j - 1]
                    cost2 = v3[k - 1]
                    cost3 = v1[j - 1][k - 1]
                    b1 = cost2 != None
                    b2 = cost1 != None and cost3 != None
                    if b1 and b2:
                        v3[k] = min(cost2 , cost1 + cost3)
                    elif b1:
                        v3[k] = cost2
                    elif b2:
                        v3[k] = cost1 + cost3

        self.A = A

    def shortestDistanceBetween(self , fromVertex , toVertex):
        return self.A[fromVertex - 1][toVertex - 1][-1]

#Read input from Hackerrank
"""n , m = map(int , raw_input().split())
edges = {i : {j : None for j in range(1 , n + 1)} for i in range(1 , n + 1)}
for _ in range(m):
    tail , head , weight = map(int , raw_input().split())
    edges[tail][head] = weight

flo = Floyd(edges)
flo.shortestDistance()
q = input()
for _ in range(q):
    fromVertex , toVertex = map(int , raw_input().split())
    print flo.shortestDistanceBetween(fromVertex , toVertex) or -1
"""

#Custom Inputs
if __name__ == "__main__":
    import time

    n = 4
    m = 5
    edges = {1 : {1 : None , 2 : 5 , 3 : None , 4 : 24} ,
    2 : {1 : None , 2 : None , 3 : None , 4 : 6} ,
    3 : {1 : None , 2 : 7 , 3 : None , 4 : 4} ,
    4 : {1 : None , 2 : None , 3 : None , 4 : None}}
    flo = Floyd(edges)
    flo.shortestDistance()
    q = 3
    fromTo = [(1 , 2) , (3 , 1) , (1 , 4)]
    for i in range(q):
        fromVertex , toVertex = fromTo[i]
        print flo.shortestDistanceBetween(fromVertex , toVertex) or -1

    start = time.time()

    results = []

    with open('floydWarshallInput.txt') as f:
        n , m = map(int , f.readline().split())
        edges = {i : {j : None for j in range(1 , n + 1)} for i in range(1 , n + 1)}
        for _ in range(m):
            tail , head , weight = map(int , f.readline().split())
            edges[tail][head] = weight

        flo = Floyd(edges)
        flo.shortestDistance()
        q = int(f.readline())
        for _ in range(q):
            fromVertex , toVertex = map(int , f.readline().split())
            results.append(flo.shortestDistanceBetween(fromVertex , toVertex) or -1)

    print "Execution time:" , time.time() - start

    with open('floydWarshallOutput.txt') as f:
        success = True
        for i in range(len(results)):
            success &= int(f.readline()) == results[i]
        print success
