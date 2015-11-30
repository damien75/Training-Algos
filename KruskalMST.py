#source Hackerrank / Algorithms / Graph Theory / Kruskal (MST): Really Special Subtree

#input: undirected graph with edges that have an integer cost

#goal: compute the Minimum Spanning Tree (MST)

#idea: We start to find out the MST by starting from a given (random) vertex
#Then, we want every time to pick the edge with minimum cost, this is why we use a heap:
#1)When we update the values in the heap, we want to make sure the the head is not already in the tree that we have,
#otherwise we will include loops further on.
#2)The heap is initialized with infinite cost for all edges, except for the edges connected to the starting vertex
#3)When we add a new vertex to the tree, we look at the other vertices this one is connected to:
#a)if the cost to one of this vertices is better than the one we had before adding this new vertex, we update it
#b)otherwise we don't change the heap
#We stop when our tree has reached the size of the graph, then we have the MST

class Heap:
    class heapElement:
        def __init__(self , node , key):
            self.node = node
            self.key = key

    def __init__(self):
        self.h = [] #stores array with 1st element: best distance and 2nd element: node in graph
        self.ref = {} #stores index in heap of a specific node

    def invariant(self , position):
        child1 = max(1 , position*2)
        child2 = child1 + 1
        maxPosition = len(self.h) - 1
        if child1 > maxPosition:
            return True
        elif child2 > maxPosition:
            return self.h[position].key <= self.h[child1].key
        else:
            return self.h[position].key <= self.h[child1].key and self.h[position].key <= self.h[child2].key

    def swap(self , p1 , p2):
        temp = self.h[p1]
        self.h[p1] = self.h[p2]
        self.h[p2] = temp
        tempRef = self.ref[self.h[p1].node]
        self.ref[self.h[p1].node] = self.ref[self.h[p2].node]
        self.ref[self.h[p2].node] = tempRef

    def bubble_up(self , position):
        parentPosition = position // 2
        while position > 0 and not self.invariant(parentPosition):
            self.swap(position , parentPosition)
            position = position // 2
            parentPosition = position // 2

    def sink_in(self , position):
        maxPosition = len(self.h) - 1
        while not self.invariant(position):
            currKey = self.h[position].key
            child1 = max(1 , position*2)
            child2 = child1 + 1
            child1Key = self.h[child1].key
            if child2 <= maxPosition and child1Key > self.h[child2].key:
                self.swap(position , child2)
                position = child2
            else:
                self.swap(position , child1)
                position = child1

    def insert(self , node , key):
        self.h.append(self.heapElement(node , key))
        self.ref[node] = len(self.h) - 1
        self.bubble_up(len(self.h) - 1)

    def delete(self , node):
        position = self.ref[node]
        maxPosition = len(self.h) - 1
        if position == maxPosition:
            node = self.h.pop().node
            self.ref.pop(node)
        else:
            self.swap(position , maxPosition)
            node = self.h.pop().node
            self.ref.pop(node)
            if self.invariant(position):
                self.bubble_up(position)
            else:
                self.sink_in(position)

    def update(self , node , key):
        self.delete(node)
        self.insert(node , key)

    def getKey(self , node):
        position = self.ref[node]
        return self.h[position].key

    def extract(self):
        extremum = self.h[0]
        self.swap(0 , len(self.h) - 1)
        node = self.h.pop().node
        self.ref.pop(node)
        self.sink_in(0)
        return extremum

def MST(edges):
    X = set()
    s = edges.keys()[0] #starting vertex chosen at random
    X.add(s)
    T = {}
    totalCost = 0
    heap = Heap() #initialize heap with values for starting vertex s
    for u in edges.keys():
        if u != s:
            heap.insert(u , float("inf"))
    for v , cost in edges[s]:
        heap.update(v , cost)
    nb_vertices = len(edges.keys())
    while len(X) < nb_vertices:
        best_v = heap.extract()
        totalCost += best_v.key
        v = best_v.node
        for w , cost in edges[v]:
            if w not in X:
                heapValue = heap.getKey(w)
                if cost < heapValue:
                    heap.update(w , cost)
        X.add(v)
    return totalCost

#Read input from Hackerrank
"""n , m = map(int , raw_input().split())
edges = {i : [] for i in range(n)}
for i in range(m):
    head , tail , cost = map(int , raw_input().split())
    head -= 1
    tail -= 1
    edges[head].append((tail , cost))
    edges[tail].append((head , cost))

print MST(edges)"""


#Custom Inputs
if __name__ == "__main__":
    edges = {0 : [(1 , 5) , (2 , 3) , (3 , 6)] ,
    1 : [(0 , 5) , (3 , 7) , (2 , 4)] ,
    2 : [(0 , 3) , (1 , 4) , (3 , 5)] ,
    3 : [(0 , 6) , (1 , 7) , (2 , 5)] }

    print MST(edges)
