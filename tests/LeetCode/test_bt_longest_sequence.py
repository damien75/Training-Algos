from unittest import TestCase

from LeetCode.binary_tree_longest_sequence import BTLongestSequence
from LeetCode.binary_tree_node import Node


class BTLongestSequenceTest(TestCase):
    def test_longest_sequence_from_bt_1(self):
        """
           1
            \
            3
           / \
          2   4
              \
               5

        Longest consecutive sequence path is 3-4-5, so return 3.
        """
        t1 = Node(1, None, Node(3, Node(2, None, None), Node(4, None, Node(5, None, None))))
        sol = BTLongestSequence(t1)
        self.assertEqual(3, sol.longest_increasing_subsequence_from_bt())

    def test_longest_sequence_from_bt_2(self):
        """
           2
            \
             3
            /
           2
          /
         1

        Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
        """
        t2 = Node(2, None, Node(3, Node(2, Node(1, None, None), None), None))
        sol = BTLongestSequence(t2)
        self.assertEqual(2, sol.longest_increasing_subsequence_from_bt())
