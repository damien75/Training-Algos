from unittest import TestCase

from LeetCode.mutable_range_sum_query import MutableRangeSum


class MutableRangeSumTest(TestCase):
    def setUp(self) -> None:
        self.instance = MutableRangeSum([1, 3, 5])

    def test_sum_range(self):
        self.assertEqual(9, self.instance.sum_range(0, 2))
        self.instance.update(1, 2)
        self.assertEqual(8, self.instance.sum_range(0, 2))
