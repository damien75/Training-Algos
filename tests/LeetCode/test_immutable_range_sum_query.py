from unittest import TestCase

from LeetCode.immutable_range_sum_query import ImmutableRangeSum


class ImmutableRangeSumTest(TestCase):
    def setUp(self) -> None:
        self.instance = ImmutableRangeSum([-2, 0, 3, -5, 2, -1])

    def test_sum_range(self):
        self.assertEqual(1, self.instance.sum_range(0, 2))
        self.assertEqual(-1, self.instance.sum_range(2, 5))
        self.assertEqual(-3, self.instance.sum_range(0, 5))
