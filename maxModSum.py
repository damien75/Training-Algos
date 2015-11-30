#input: array ar and integer M

#goal: compute the max sum of elements of ar modulo M

#idea: construct a previx sum st prefix[i] = sum(ar[:i]) %M
#we also have sum(ar[a..i]) = (prefix[i] - prefix[a]) %M
#we want to choose a st prefix[a] is bigger than prefix[i] but the smallest possible, so that the diff % M will be close to M
#then we can use a binary search to find for which a we can have this best prefix[a] that fits our needs

class BST:
    class TreeNode:
        def __init__(self , key , left=None , right=None , parent=None):
            self.key = key
            self.leftChild = left
            self.rightChild = right
            self.parent = parent

        def hasLeftChild(self):
            return self.leftChild

        def hasRightChild(self):
            return self.rightChild

        def isLeftChild(self):
            return self.parent and self.parent.leftChild == self

    def __init__(self):
        self.root = None

    def insert(self , key):
        if self.root:
            self.insertNode(key , self.root)
        else:
            self.root = self.TreeNode(key)

    def insertNode(self , key , currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self.insertNode(key , currentNode.leftChild)
            else:
                   currentNode.leftChild = self.TreeNode(key , parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self.insertNode(key , currentNode.rightChild)
            else:
                   currentNode.rightChild = self.TreeNode(key , parent=currentNode)

    def findNodeOrNext(self , key , currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild() and key < self.findMax(currentNode).key:
                   return self.findNodeOrNext(key , currentNode.leftChild)
            else:
                   return currentNode
        elif key == currentNode.key:
            return currentNode
        else:
            if currentNode.hasRightChild():
                   return self.findNodeOrNext(key , currentNode.rightChild)
            else:
                   return currentNode

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                  return res.payload
            else:
                  return None
        else:
            return None

    def _get(self , key , currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
         return self.get(key)

    def __contains__(self,key):
         return self._get(key , self.root)

    def findNext(self , value):
        succ = None
        if not self.root: #if tree empty then return
            return succ
        else:
            currMax = self.findMax(self.root).key
            if value > currMax: #if we try to find the next value for a value already > max of the tree, return
                return succ
            else:
                node = self.findNodeOrNext(value , self.root) #get the node of the tree right after the given value
                if node.key > value:
                    return node
                else:
                    if node.hasRightChild():
                        succ = self.findMin(node.rightChild)
                    else:
                        if node.parent:
                            if node.isLeftChild():
                                succ = node.parent
                            else:
                                node.parent.rightChild = None
                                succ = self.findNext(node.parent.key)
                                node.parent.rightChild = node
                    return succ

    def findMin(self , fromNode):
        current = self._get(fromNode.key , self.root)
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findMax(self , fromNode):
        current = self._get(fromNode.key , self.root)
        while current.hasRightChild():
            current = current.rightChild
        return current

def maxSumModulo(ar , M):
    if len(ar) == 0:
        return 0
    else:
        prefix = [0]*len(ar)
        prefix[0] = ar[0] % M
        bestSum = prefix[0]
        tree = BST()
        for i in range(len(ar)):
            if i > 0:
                prefix[i] = (prefix[i-1] + ar[i]) % M
            maxSum = prefix[i]
            prevSum = tree.findNext(prefix[i]) # finds the "next", aka smallest, number bigger than the argument
            if prevSum:
                maxSum = (prefix[i] - prevSum.key) % M
            bestSum = max(bestSum, maxSum)
            tree.insert(prefix[i])
        return bestSum

def solveFromCustomInput():
    with open("maxSum test1.txt") as f:
        t = int(f.readline())
        result = []
        for _ in range(t):
            n , M = map(int , f.readline().split())
            ar = map(int , f.readline().split())
            result.append(maxSumModulo(ar , M))

    return result

#Read the input from Hackerrank
"""t = input()
for _ in range(t):
    n , M = map(int , raw_input().split())
    ar = map(int , raw_input().split())
    print maxSumModulo(ar , M)"""

if __name__ == "__main__":
    #import timeit
    #t = timeit.Timer('solveFromCustomInput()', 'from __main__ import solveFromCustomInput')

    result = solveFromCustomInput()
    print result
    with open("maxSum output1.txt") as f:
        success = True
        for i in range(len(result)):
            success &= int(f.readline()) == result[i]
        print success
    #print t.timeit(number=1)
