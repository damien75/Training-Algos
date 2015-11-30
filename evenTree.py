#source Hackerrank / Algorithms / Graph Theory / Even Tree

#input: Tree

#goal: cut the max number of edges st each subtree we get has an odd nb of vertices

#idea: build tree and then go through tree to count nb of children

class cutTree:
    def __init__(self , edges , N , M):
        self.edges = edges
        self.N = N
        self.M = M
        self.tree = []

    def findChildren(self , n):
        children = []
        for x in range(self.M):
            if edges[x][1] == n:
                children.append(self.edges[x][0])
                childN = self.findChildren(self.edges[x][0])
                for child in childN:
                    children.append(child)
        return children

    def generateTree(self):
        for x in range(self.N):
    		self.tree.append([x+1])
        for x in range(self.N):
    		self.tree[x].append(self.findChildren(x+1))
        return self.tree

    def numberEdgesToRemove(self):
        self.generateTree()

        count = 0
        for x in range(self.N):
            if len(self.tree[x][1]) % 2 == 1:
                count += 1
        return count - 1

#Read input from Hackerrank
"""N, M = map(int, raw_input().split())
edges = []
for x in xrange(M):
    u, v = map(int, raw_input().split())
    edges.append([u, v])"""

#Custom Inputs
if __name__ == "__main__":
    N = 10
    M = 9
    edges = [(2 , 1) ,
    (3 , 1),
    (4 , 3),
    (5 , 2),
    (6 , 1),
    (7 , 2),
    (8 , 6),
    (9 , 8),
    (10 ,8)]

    cut = cutTree(edges , N , M)
    print cut.numberEdgesToRemove()
