#source Facebook interview question

#input: binary tree

#goal: return an array with the nodes of the tree sorted with 2 priorities:
#1. left to right
#2. if nodes are on the same distance from the left, sort top to bottom

#idea: we are going to go through the tree using BFS so that we already have the 2nd
#condition satisfied in this way.
#For each node we see, we will have a index showing how far (left or right) we are from
#the root.
#For each node we see, we are going to access the data structure we use to look if we already
#have nodes at this same distance, if yes we append this new node at the end of the list;
#and if not just add a new list with only this node in it.

#Data structure: for each node we see, we are going to do 1 lookup and 1 insertion
#At the end we will just output all the nodes with smallest index first and largest index
#last ==> therefore the good data structure for this problem is a hashtable

class SideViewBinaryTree:
    def __init__(self):
        self.toVisit = []
        self.h = {}
        self.min = None

    def addNodeToHashMap(self , node , index):
        if index in self.h:
            self.h[index].append(node.key)
        else:
            self.h[index] = [node.key]

    def addChildrenToVisit(self , node , index):
        if node.right is not None:
            self.toVisit.append((node.right , index + 1))
        if node.left is not None:
            self.toVisit.append((node.left , index - 1))

    def orderNodesInTree(self , start):
        self.min = 0
        self.toVisit = [(start , 0)]
        while len(self.toVisit) > 0:
            node , index = self.toVisit.pop(0)
            self.min = min(index , self.min)
            self.addNodeToHashMap(node , index)
            self.addChildrenToVisit(node , index)

    def outputResult(self , start):
        self.orderNodesInTree(start)
        result = []
        index = self.min
        while index in self.h:
            result.extend(self.h[index])
            index += 1
        return result

class Node:
    def __init__(self , key , left , right):
        self.key = key
        self.left = left
        self.right = right

#Input 1:

#      6
#     / \
#    3   4
#     \
#      1

root1 = Node(6 , Node(3 , None , Node(1 , None , None)) , Node(4 , None , None))

v1 = SideViewBinaryTree()
view1 = v1.outputResult(root1)
print "Output 1 should be: 3 6 1 4"
print "Actual output: " , view1

#Input 2:

#      6
#     / \
#    3   4
#   / \   \
#  5   1   0
# / \     /
#9   2   8
#     \
#      7

root2 = Node(6 , Node(3 , Node(5 , Node(9 , None , None) , Node(2 , None , Node(7 , None , None))) , Node(1 , None , None)),
         Node(4 , None , Node(0 , Node(8 , None , None) , None)))

v2 = SideViewBinaryTree()
view2 = v2.outputResult(root2)
print "Output 2 should be: 9 5 3 2 6 1 7 4 8 0"
print "Actual output: " , view2
