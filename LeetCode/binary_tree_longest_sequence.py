from LeetCode.binary_tree_node import Node


class BTLongestSequence:
    """
    Input : Binary Tree

    Goal: Find the length of the longest CONSECUTIVE INCREASING sequence in that tree
    the sequence has to go from parent to child and not the reverse

    Idea: Do a BFS from root and keep track of the best result seen so far
    if value of child on right is curr + 1, then increase curr length - same for left
    recursive approach

    complexity: O(n) for a tree with n nodes in time and O(n) in space
    """

    def __init__(self, root: Node):
        self.root = root
        self.res = 0

    def longest_increasing_subsequence_from_bt(self):
        if self.root is None:
            return 0
        self.recursive_longest_subsequence(self.root, 1)
        return self.res

    def recursive_longest_subsequence(self, curr: Node, max_length: int):
        self.res = max(self.res, max_length)
        if curr.left is not None:
            left = max_length + 1 if curr.left.key == curr.key + 1 else 1
            self.recursive_longest_subsequence(curr.left, left)
        if curr.right is not None:
            right = max_length + 1 if curr.right.key == curr.key + 1 else 1
            self.recursive_longest_subsequence(curr.right, right)
