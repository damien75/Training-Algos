#input : Binary Tree

#goal: Find the length of the longest CONSECUTIVE INCREASING sequence in that tree
#the sequence has to go from parent to child and not the reverse

#idea: Do a BFS from root and keep track of the best result seen so far
#if value of child on right is curr + 1, then increase curr length - same for left
#recursive approach

#complexity: O(n) for a tree with n nodes in time and O(n) in space

from binaryTree import Node

class Solution:
    def __init__(self , root):
        self.root = root
        self.res = 0

    def longestIncreasingSubSequenceFromBT(self):
        if self.root is None:
            return 0
        self.recursiveLongestSubsequence(self.root , 1)
        return self.res

    def recursiveLongestSubsequence(self , curr , maxLength):
        self.res = max(self.res , maxLength)
        if curr.left is not None:
            left = maxLength + 1 if curr.left.key == curr.key + 1 else 1
            self.recursiveLongestSubsequence(curr.left , left)
        if curr.right is not None:
            right = maxLength + 1 if curr.right.key == curr.key + 1 else 1
            self.recursiveLongestSubsequence(curr.right , right)

#For example,
#   1
#    \
#     3
#    / \
#   2   4
#       \
#        5
#Longest consecutive sequence path is 3-4-5, so return 3.
t1 = Node(1 , None , Node(3 , Node(2 , None , None) , Node(4 , None , Node(5 , None , None))))
sol = Solution(t1)
print sol.longestIncreasingSubSequenceFromBT() , "should be equal to" , 3
#   2
#    \
#     3
#    /
#   2
#  /
# 1
#Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
t2 = Node(2 , None , Node(3 , Node(2 , Node(1 , None , None) , None) , None))
sol = Solution(t2)
print sol.longestIncreasingSubSequenceFromBT() , "should be equal to" , 2
