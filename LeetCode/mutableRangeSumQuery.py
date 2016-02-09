#input : array of n integers

#goal: Be able to compute the most efficiently possible the sum in a given range and the update of a given value
#Indeed a lot of calls will be made to the sumRange and update functions

#idea: Use a segment tree to be able to access sums and update frequently and for minimum cost

#complexity: O(n log n) in time to build the tree and then O(log n) for each call to sumRange or update and O(n log n) in space

class MutableRangeSum:
    class Node:
        def __init__(self , start , end):
            self.sum = 0
            self.start = start
            self.end = end
            self.left = None
            self.right = None

    def buildSegmentTree(self , start , end):
        if start > end:
            return None
        cur = self.Node(start , end)
        if start == end:
            cur.sum = self.ar[start]
        else:
            mid = start + (end - start)/2
            cur.left = self.buildSegmentTree(start , mid)
            cur.right = self.buildSegmentTree(mid + 1 , end)
            cur.sum = cur.left.sum + cur.right.sum
        return cur

    def __init__(self , ar):
        self.ar = ar
        self.root = self.buildSegmentTree(0 , len(ar) - 1)

    def update(self , i , val , root = None):
        if root is None:
            root = self.root
        if root.start == root.end: #this is a leaf
            root.sum = val
        else:
            mid = root.start + (root.end - root.start)/2
            if i <= mid:
                self.update(i , val , root.left)
            else:
                self.update(i , val , root.right)
            root.sum = root.left.sum + root.right.sum

    def sumRange(self , i , j , root = None):
        if root is None:
            root = self.root
        if i == root.start and j == root.end:
            return root.sum
        else:
            mid = root.start + (root.end - root.start)/2
            if j <= mid:
                return self.sumRange(i , j , root.left)
            elif i > mid:
                return self.sumRange(i , j , root.right)
            else:
                return self.sumRange(i , mid , root.left) + self.sumRange(mid + 1 , j , root.right)

#Example:
nums = [1, 3, 5]

mutable = MutableRangeSum(nums)
print mutable.sumRange(0, 2) , "should be" , 9
mutable.update(1, 2)
print mutable.sumRange(0, 2) , "should be" , 8
