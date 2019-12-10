#source Hackerrank / Algorithms / Search / Maximize Sum

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

    def findNext(self , key , currentNode): #return key + 1 or bigger
        if not currentNode:
            return None
        elif key + 1 == currentNode.key:
            return currentNode
        elif key + 1 < currentNode.key:
            return self.findNext(key , currentNode.leftChild) or currentNode
        else:
            return self.findNext(key , currentNode.rightChild)

    def invariant(self , node , key):
        if not node:
            return None
        elif key + 1 == node.key:
            return "this"
        elif key + 1 < node.key:
            return "left"
        else:
            return "right"

    def findNextIterative(self , key): #return key + 1 or bigger
        node = self.root
        if not node:
            return None
        inv = self.invariant(node , key)
        nodes = [key]
        while inv:
            nodes.append(node.key)
            if inv == "this":
                break
            elif inv == "left":
                node = node.leftChild
                inv = self.invariant(node , key)
            else:
                node = node.rightChild
                inv = self.invariant(node , key)
        nodes = sorted(nodes)
        if nodes[-1] == key:
            return None
        else:
            return nodes[nodes.index(key) + 1]

def maxSumModulo(ar , M):
    if len(ar) == 0:
        return 0
    else:
        prefix = [0 for _ in range(len(ar))]
        bestSum = prefix[0] % M
        tree = BST()
        for i in range(len(ar)):
            if i > 0:
                prefix[i] = (prefix[i-1] + ar[i]) % M
            else:
                prefix[i] = ar[i] % M
            maxSum = prefix[i]
            #prevSum = tree.findNextIterative(prefix[i])
            prevSum = tree.findNext(prefix[i] , tree.root) # finds the "next", aka smallest, number bigger than the argument
            if prevSum:
                maxSum = (prefix[i] - prevSum.key) % M
            bestSum = max(bestSum, maxSum)
            if bestSum == M - 1:
                break
            tree.insert(prefix[i])
        return bestSum

def findSmallestGreaterThan(nextNb , maxSum):
    i = bisect.bisect_right(nextNb, maxSum)
    prevSum = None
    if i < len(nextNb):
        prevSum = nextNb[i]
    return prevSum

def maxSumModuloWithoutTree(ar , M):
    if len(ar) == 0:
        return 0
    else:
        prefix = [0 for _ in range(len(ar))]
        bestSum = prefix[0] % M
        nextNb = []
        for i in range(len(ar)):
            if i > 0:
                prefix[i] = (prefix[i-1] + ar[i]) % M
            else:
                prefix[i] = ar[i] % M
            maxSum = prefix[i]
            prevSum = findSmallestGreaterThan(nextNb , maxSum) # finds the "next", aka smallest, number bigger than the argument
            if prevSum:
                maxSum = (maxSum - prevSum) % M
            bestSum = max(bestSum, maxSum)
            if bestSum == M - 1:
                break
            bisect.insort(nextNb , prefix[i]) #insert the new prefix in the array bisection, which allows binary search more efficiently than BST
        return bestSum

def solveFromCustomInput():
    with open("maxSum test1.txt") as f:
        t = int(f.readline())
        result = []
        for _ in range(t):
            n , M = map(int , f.readline().split())
            ar = map(int , f.readline().split())
            result.append(maxSumModuloWithoutTree(ar , M))

    return result

#Read the input from Hackerrank
"""t = input()
for _ in range(t):
    n , M = map(int , raw_input().split())
    ar = map(int , raw_input().split())
    print maxSumModulo(ar , M)"""

if __name__ == "__main__":
    import time , bisect

    start = time.time()
    result = solveFromCustomInput()
    with open("maxSum output1.txt") as f:
        success = True
        for i in range(len(result)):
            success &= int(f.readline()) == result[i]
        print success
    print "Execution time:" , time.time() - start
