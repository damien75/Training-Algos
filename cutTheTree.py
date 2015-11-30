#source Hackerrank / Algorithms / Search

#input: tree with weights

#goal: cut in 2 trees with minimal total weight difference

#idea: keep a dict of the connected nodes and a list of the weights
#Using DFS with a set of visited nodes and a stack of nodes to visit,
#Add the weight of the current subtree to the parent so that sutTotals gives the weight of the subtree when we move up
#subTotals : node => weight of its subtree with node as root
#and the best difference so far

def minDiffCut(graph, weights , vertex):
    total = sum(weights)
    visited = set()
    bestDiff = total
    toVisit = [vertex]
    toVisitSet = set() #Adding this set instead of just having the toVisit list increases speed drastically when checking if next_vtx has already been seen and is in the toVisit
    toVisitSet.add(vertex)
    subTotals = {vertex : weights[vertex] for vertex in graph.keys()}
    while len(toVisit) > 0:
        currVertex = toVisit[-1]
        hasChildrenNotVisited = False
        for next_vtx in graph[currVertex]:
            if next_vtx in visited or next_vtx in toVisitSet: #we need to check if it is in the list to visit but is not yet considered visited, even if it's in the list
                continue
            toVisit.append(next_vtx)
            toVisitSet.add(next_vtx)
            hasChildrenNotVisited = True
        if not hasChildrenNotVisited:
            visited.add(currVertex)
            toVisit.pop() #we have visited all its children, we can now remove this node from the list to visit
            for next_vtx in graph[currVertex]:
                if next_vtx not in visited:
                    subTotals[next_vtx] += subTotals[currVertex] #we update the weight of its parent
            bestDiff = min(bestDiff, abs(2*subTotals[currVertex] - total))
    return bestDiff

#Lines to get the input from Hackerrank
"""nbNodes = input()
weights = map(int , raw_input().split())
tree = {i : [] for i in range(nbNodes)}
for _ in range(nbNodes - 1):
    parent , child = map(int , raw_input().split())
    tree[parent - 1].append(child - 1)
    tree[child - 1].append(parent - 1)"""

#Custom input
nbNodes = 6
weights = [100 , 200 , 100 , 500 , 100 , 600]
tree = {0 : [1] , 1 : [0 , 2 , 4] , 2 : [3] , 3 : [4] , 4 : [1 , 3 , 5] , 5 : [4]}

print minDiffCut(tree , weights , 0)
