from typing import Optional, Tuple, List, Dict


class Node:
    def __init__(self, key: int, left, right):
        """
        :type left: Optional[Node]
        :type right: Optional[Node]
        """
        self.key = key
        self.left = left
        self.right = right


class SideViewBinaryTree:
    """
    Source Facebook interview question

    Input: binary tree

    Goal: return an array with the nodes of the tree sorted with 2 priorities:
    1. left to right
    2. if nodes are on the same distance from the left, sort top to bottom

    Idea: we are going to go through the tree using BFS so that we already have the 2nd
    condition satisfied in this way.
    For each node we see, we will have a index showing how far (left or right) we are from
    the root.
    For each node we see, we are going to access the data structure we use to look if we already
    have nodes at this same distance, if yes we append this new node at the end of the list;
    and if not just add a new list with only this node in it.

    Data structure: for each node we see, we are going to do 1 lookup and 1 insertion
    At the end we will just output all the nodes with smallest index first and largest index
    last ==> therefore the good data structure for this problem is a hashtable
    """

    def __init__(self):
        self.toVisit: List[Tuple[Node, int]] = []
        self.h: Dict[int, List[int]] = {}
        self.min: Optional[int] = None

    def add_node_to_hashmap(self, node: Node, index: int):
        if index in self.h:
            self.h[index].append(node.key)
        else:
            self.h[index] = [node.key]

    def add_children_to_visit(self, node: Node, index: int):
        if node.right is not None:
            self.toVisit.append((node.right, index + 1))
        if node.left is not None:
            self.toVisit.append((node.left, index - 1))

    def order_nodes_in_tree(self, start: Node):
        self.min = 0
        self.toVisit = [(start, 0)]
        while len(self.toVisit) > 0:
            node, index = self.toVisit.pop(0)
            self.min = min(index, self.min)
            self.add_node_to_hashmap(node, index)
            self.add_children_to_visit(node, index)

    def output_result(self, start: Node) -> List[int]:
        self.order_nodes_in_tree(start)
        result = []
        index = self.min
        while index in self.h:
            result.extend(self.h[index])
            index += 1
        return result
