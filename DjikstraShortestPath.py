#source Hackerrank / Algorithms / Graph Theory / Dijkstra: Shortest Reach 2

#input: undirected graph with integer (positive) edge costs

#goal: given a starting vertex, compute the shortest path to every other vertex, -1 if unreachable

#idea: keep an hashtable A that gives the length of the shortest path to get from s to a given vertex v
#Use a PriorityQueue pq as a heap, where the min cost edge crossing the boundary between seen and not yet seen vertices
#while pq is not empty:
#   use heap to get the shortest edge with tail seen and head outside of X
#   A[head] = A[tail] + len(edge[tail -> head])
#   updateEdgesCrossingBoundary

import Queue

class Djikstra:
    def __init__(self , graph):
        self.graph = graph

    def updateEdgesCrossingBoundary(self , tail , A , pq):
        for head in self.graph[tail].keys():
            pq.put((A[tail] + self.graph[tail][head] , head))

    def DjikstraWithHeap(self , s):
        A = {s : 0}
        nb_vertices = len(self.graph.keys())
        pq = Queue.PriorityQueue()
        self.updateEdgesCrossingBoundary(s , A , pq)
        while not pq.empty():
            cost , v = pq.get()
            if v in A:
                continue
            A[v] = cost
            self.updateEdgesCrossingBoundary(v , A , pq)
        for i in self.graph.keys(): #put -1 for unreachable vertices
            if i not in A:
                A[i] = -1
        A.pop(s) #remove the start vertex from the hashtable
        return [A[v] for v in sorted(A.keys())]

#Read input from Hackerrank
"""t = input()

for i in range(t):
    n , m = map(int , raw_input().split())
    edges = {}
    for j in range(m):
        tail , head , cost = map(int , raw_input().split())
        if tail in edges:
            if head in edges[tail]:
                edges[tail][head] = min(edges[tail][head] , cost)
            else:
                edges[tail][head] = cost
        else:
            edges[tail] = {}
            edges[tail][head] = cost
        if head in edges:
            if tail in edges[head]:
                edges[head][tail] = min(edges[head][tail] , cost)
            else:
                edges[head][tail] = cost
        else:
            edges[head] = {}
            edges[head][tail] = cost
    start = input()

    Djik = Djikstra(edges)

    for dis in Djik.DjikstraWithHeap(start):
        print dis,
    print"""

#Custom Inputs
edges = {1 : {2 : 24 , 3 : 3} , 2 : {1 : 24} , 3 : {1 : 3 , 4 : 12} , 4 : {1 : 20 , 3 : 12}}
start = 1

Djik = Djikstra(edges)

for dis in Djik.DjikstraWithHeap(start):
    print dis,
print
