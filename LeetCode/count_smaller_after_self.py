from typing import List

from LeetCode.binary_tree_node import Node


class SmallerElements(object):
    """
    Input : integer array ar

    Goal: Count at each position in the array the number of smaller elements that will show in the right side of the
    array from this element

    Idea: go through array from right to left
    when we see new element:
       use a binary tree keeping track of the number of elements to its left, ie the nb of smaller elements
       if the new element is larger than the current node in tree:
           increase the count for this element by the current node count
           go to the right
       if new element is smaller:
           increase the count for the current node by 1
           go to the left


    complexity: O(n log(n)) in the worst case in time and O(n) in space
    """

    @staticmethod
    def count_smaller_elements(ar: List[int]) -> List[int]:
        result = [0]
        root = None
        for el in reversed(ar):
            count = 0
            if root is None:
                root = Node(el, None, None)
                continue
            current = root
            while True:
                if el < current.key:
                    current.count += 1
                    if current.left is None:
                        current.left = Node(el, None, None)
                        break
                    else:
                        current = current.left
                else:
                    count += current.count + 1
                    if current.right is None:
                        current.right = Node(el, None, None)
                        break
                    else:
                        current = current.right
            result.append(count)
        result.reverse()
        return result
