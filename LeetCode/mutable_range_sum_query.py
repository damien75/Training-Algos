from typing import List, Optional


class MutableRangeSum:
    """
    Input : array of n integers

    Goal: Be able to compute the most efficiently possible the sum in a given range and the update of a given value
    Indeed a lot of calls will be made to the sumRange and update functions

    Idea: Use a segment tree to be able to access sums and update frequently and for minimum cost

    complexity: O(n log n) in time to build the tree and then O(log n) for each call to sumRange or update
    and O(n log n) in space
    """

    class Node:
        def __init__(self, start: int, end: int):
            self.sum = 0
            self.start = start
            self.end = end
            self.left = None
            self.right = None

    def build_segment_tree(self, start: int, end: int):
        if start > end:
            return None
        cur = self.Node(start, end)
        if start == end:
            cur.sum = self.ar[start]
        else:
            mid = start + (end - start) // 2
            cur.left = self.build_segment_tree(start, mid)
            cur.right = self.build_segment_tree(mid + 1, end)
            cur.sum = cur.left.sum + cur.right.sum
        return cur

    def __init__(self, ar: List[int]):
        self.ar = ar
        self.root = self.build_segment_tree(0, len(ar) - 1)

    def update(self, i: int, val: int, root: Optional[Node] = None):
        if root is None:
            root = self.root
        if root.start == root.end:  # this is a leaf
            root.sum = val
        else:
            mid = root.start + (root.end - root.start) / 2
            if i <= mid:
                self.update(i, val, root.left)
            else:
                self.update(i, val, root.right)
            root.sum = root.left.sum + root.right.sum

    def sum_range(self, i: int, j: int, root: Optional[Node] = None):
        if root is None:
            root = self.root
        if i == root.start and j == root.end:
            return root.sum
        else:
            mid = root.start + (root.end - root.start) // 2
            if j <= mid:
                return self.sum_range(i, j, root.left)
            elif i > mid:
                return self.sum_range(i, j, root.right)
            else:
                return self.sum_range(i, mid, root.left) + self.sum_range(mid + 1, j, root.right)
