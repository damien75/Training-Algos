from bisect import bisect_right, insort

from typing import List, Optional


class BST:
    class TreeNode:
        def __init__(self, key: int, left=None, right=None, parent=None):
            self.key = key
            self.leftChild = left
            self.rightChild = right
            self.parent = parent

        def has_left_child(self):
            return self.leftChild

        def has_right_child(self):
            return self.rightChild

    def __init__(self):
        self.root = None

    def insert(self, key: int):
        if self.root:
            self.insert_node(key, self.root)
        else:
            self.root = self.TreeNode(key)

    def insert_node(self, key: int, current_node: TreeNode):
        if key < current_node.key:
            if current_node.has_left_child():
                self.insert_node(key, current_node.leftChild)
            else:
                current_node.leftChild = self.TreeNode(key, parent=current_node)
        else:
            if current_node.has_right_child():
                self.insert_node(key, current_node.rightChild)
            else:
                current_node.rightChild = self.TreeNode(key, parent=current_node)

    def find_next(self, key, current_node) -> Optional[TreeNode]:  # return key + 1 or bigger
        if not current_node:
            return None
        elif key + 1 == current_node.key:
            return current_node
        elif key + 1 < current_node.key:
            return self.find_next(key, current_node.leftChild) or current_node
        else:
            return self.find_next(key, current_node.rightChild)

    @staticmethod
    def invariant(node: TreeNode, key: int):
        if not node:
            return None
        elif key + 1 == node.key:
            return "this"
        elif key + 1 < node.key:
            return "left"
        else:
            return "right"

    def find_next_iterative(self, key: int) -> Optional[List[int]]:  # return key + 1 or bigger
        node = self.root
        if not node:
            return None
        inv = self.invariant(node, key)
        nodes = [key]
        while inv:
            nodes.append(node.key)
            if inv == "this":
                break
            elif inv == "left":
                node = node.leftChild
                inv = self.invariant(node, key)
            else:
                node = node.rightChild
                inv = self.invariant(node, key)
        nodes = sorted(nodes)
        if nodes[-1] == key:
            return None
        else:
            return nodes[nodes.index(key) + 1]


class MaxModuloSum(object):
    """
    Source Hackerrank / Algorithms / Search / Maximize Sum

    Input: array ar and integer M

    Goal: compute the max sum of elements of ar modulo M

    Idea: construct a previx sum st prefix[i] = sum(ar[:i]) %M
    we also have sum(ar[a..i]) = (prefix[i] - prefix[a]) %M
    we want to choose a st prefix[a] is bigger than prefix[i] but the smallest possible, so that the diff % M
    will be close to M
    then we can use a binary search to find for which a we can have this best prefix[a] that fits our needs
    """

    @staticmethod
    def max_sum_modulo(ar: List[int], m: int) -> int:
        if len(ar) == 0:
            return 0
        else:
            prefix = [0 for _ in range(len(ar))]
            best_sum = prefix[0] % m
            tree = BST()
            for i in range(len(ar)):
                if i > 0:
                    prefix[i] = (prefix[i - 1] + ar[i]) % m
                else:
                    prefix[i] = ar[i] % m
                max_sum = prefix[i]
                prev_sum = tree.find_next(prefix[i], tree.root)
                # finds the "next", aka smallest, number bigger than the argument
                if prev_sum:
                    max_sum = (prefix[i] - prev_sum.key) % m
                best_sum = max(best_sum, max_sum)
                if best_sum == m - 1:
                    break
                tree.insert(prefix[i])
            return best_sum

    @staticmethod
    def find_smallest_greater_than(next_nb: List[int], max_sum: int) -> int:
        i = bisect_right(next_nb, max_sum)
        prev_sum = None
        if i < len(next_nb):
            prev_sum = next_nb[i]
        return prev_sum

    def max_sum_modulo_without_tree(self, ar: List[int], m: int) -> int:
        if len(ar) == 0:
            return 0
        else:
            prefix = [0 for _ in range(len(ar))]
            best_sum = prefix[0] % m
            next_nb = []
            for i in range(len(ar)):
                if i > 0:
                    prefix[i] = (prefix[i - 1] + ar[i]) % m
                else:
                    prefix[i] = ar[i] % m
                max_sum = prefix[i]
                prev_sum = self.find_smallest_greater_than(next_nb, max_sum)
                # finds the "next", aka smallest, number bigger than the argument
                if prev_sum:
                    max_sum = (max_sum - prev_sum) % m
                best_sum = max(best_sum, max_sum)
                if best_sum == m - 1:
                    break
                insort(next_nb, prefix[i])
                # insert the new prefix in the array bisection, which allows binary search more efficiently than BST
            return best_sum

    def solve_from_custom_input(self, file_path: str) -> List[int]:
        with open(file_path) as f:
            t = int(f.readline())
            result = []
            for _ in range(t):
                n, m = map(int, f.readline().split())
                ar = list(map(int, f.readline().split()))
                result.append(self.max_sum_modulo_without_tree(ar, m))

        return result

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())
        for _ in range(t):
            n, m = map(int, input().split())
            ar = list(map(int, input().split()))
            print(self.max_sum_modulo(ar, m))
