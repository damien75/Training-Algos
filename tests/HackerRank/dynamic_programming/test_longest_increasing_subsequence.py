from unittest import TestCase

from HackerRank.dynamic_programming.longest_increasing_subsequence import LongestIncreasingSubsequence


class LongestIncreasingSubsequenceTest(TestCase):
    def setUp(self) -> None:
        self.instance = LongestIncreasingSubsequence()

    def test_get_lis_1(self):
        a = [29471, 5242, 21175, 28931, 2889, 7275, 19159, 21773, 1325, 6901]
        self.assertEqual(4, self.instance.length_of_longest_subsequence(a))

    def test_get_lis_2(self):
        a = [2, 7, 4, 3, 8]
        self.assertEqual(3, self.instance.length_of_longest_subsequence(a))
