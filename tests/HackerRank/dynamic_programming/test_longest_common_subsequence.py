from unittest import TestCase

from HackerRank.dynamic_programming.longest_common_subsequence import LongestCommonSubsequence


class LongestCommonSubsequenceTest(TestCase):
    def setUp(self) -> None:
        self.instance = LongestCommonSubsequence()

    def test_get_lcs_int_array(self):
        list_a = [1, 2, 3, 4, 1]
        list_b = [3, 4, 1, 2, 1, 3]
        self.assertEqual([3, 4, 1], self.instance.longest(list_a, list_b))
        self.assertEqual([1, 2, 3], self.instance.longest(list_b, list_a))

    def test_get_lcs_char_array(self):
        list_a = ['G', 'A', 'C']
        list_b = ['A', 'G', 'C', 'A', 'T']
        self.assertEqual(['A', 'C'], self.instance.longest(list_a, list_b))
        self.assertEqual(['G', 'A'], self.instance.longest(list_b, list_a))
