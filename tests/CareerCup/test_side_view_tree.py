from unittest import TestCase

from CareerCup.side_view_tree import Node, SideViewBinaryTree


class SideViewBinaryTreeTest(TestCase):
    def setUp(self) -> None:
        self.instance = SideViewBinaryTree()

    def test_get_side_view1(self):
        """
              6
             / \
           3   4
            \
            1
        """
        root1 = Node(6, Node(3, None, Node(1, None, None)), Node(4, None, None))

        self.assertEqual([3, 6, 1, 4], self.instance.output_result(root1))

    def test_get_side_view2(self):
        """
              6
             / \
            3   4
           / \   \
          5   1   0
         / \     /
        9   2   8
            \
            7
        """

        root2 = Node(6, Node(3, Node(5, Node(9, None, None), Node(2, None, Node(7, None, None))), Node(1, None, None)),
                     Node(4, None, Node(0, Node(8, None, None), None)))

        self.assertEqual([9, 5, 3, 2, 6, 1, 7, 4, 8, 0], self.instance.output_result(root2))
