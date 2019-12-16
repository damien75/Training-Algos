from typing import Optional


class Node:
    def __init__(self, key: int, left, right):
        """
        :type left: Optional[Node]
        :type right: Optional[Node]
        """
        self.key = key
        self.count = 0
        self.left = left
        self.right = right
