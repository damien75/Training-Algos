#input : number of nodes n and list of undirected edges

#goal: Find the number of connected components in the graph

#idea: Use a union find data structure and then output the number of connected components

#complexity: 0(n^2) building data structure in worst case in time and 0(n) in space

class UF:
    def __init__(self , n):
        self.ids = [i for i in range(n)]
        self.count = n

    def union(self , id1 , id2):
        i1 = self.ids[id1]
        i2 = self.ids[id2]
        if i1 != i2:
            for i in range(len(self.ids)):
                if self.ids[i] == i2:
                    self.ids[i] = i1
            self.count -= 1

    def isConnected(self , id1 , id2):
        return self.ids[id1] == self.ids[id2]


#Example 1:
#     0          3
#     |          |
#     1 --- 2    4
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
#expect to return 2.
uf = UF(n)
for e in edges:
    uf.union(e[0] , e[1])
print uf.count

#Example 2:
#     0           4
#     |           |
#     1 --- 2 --- 3
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#expect to return 1.
uf = UF(n)
for e in edges:
    uf.union(e[0] , e[1])
print uf.count
