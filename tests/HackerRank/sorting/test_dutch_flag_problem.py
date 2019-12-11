from unittest import TestCase

from HackerRank.sorting.dutch_flag_problem import DutchFlag


class DutchFlagTest(TestCase):
    def setUp(self) -> None:
        self.instance = DutchFlag()

    def test_partition_flag(self):
        self.assertEqual([3, 1, 0, 2, 8, 4, 6, 9, 9], self.instance.partition([3, 1, 4, 9, 8, 2, 6, 9, 0], 4, 8))
