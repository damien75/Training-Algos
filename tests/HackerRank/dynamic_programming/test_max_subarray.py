from unittest import TestCase

from HackerRank.dynamic_programming.max_sub_array import MaxSubArray


class MaxSubArrayTest(TestCase):
    def setUp(self) -> None:
        self.instance = MaxSubArray()

    def test_get_max_sub_array_1(self):
        self.assertEqual((10, 10), self.instance.compute_best_sum([1, 2, 3, 4]))

    def test_get_lis_2(self):
        self.assertEqual((10, 11), self.instance.compute_best_sum([2, -1, 2, 3, 4, -5]))
