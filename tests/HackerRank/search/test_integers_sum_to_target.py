from unittest import TestCase

from HackerRank.search.integers_sum_to_target import SumToTarget


class SumToTargetTest(TestCase):
    def setUp(self) -> None:
        self.instance = SumToTarget()

    def test_sum_to_target_3(self):
        self.assertEqual([(-3, 0, 3), (-3, 1, 2), (-2, -1, 3), (-2, 0, 2), (-2, 0, 2), (-1, 0, 1)],
                         self.instance.get_sets_of_three_that_sum_to_target([2, 3, 1, -2, -1, 0, 2, -3, 0], 0))

    def test_sum_to_target_2(self):
        self.assertEqual([(2, 0), (3, -1), (1, 1), (-1, 3), (0, 2), (2, 0), (0, 2)],
                         self.instance.get_sets_of_two_that_sum_to_target([2, 3, 1, -2, -1, 0, 2, -3, 0], 2))
