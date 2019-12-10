from unittest import TestCase

from HackerRank.dynamic_programming.knapsack import Knapsack


class KnapsackTest(TestCase):
    def test_walk_grid(self):
        max_capacity = 12
        values = [1, 6, 9]
        knapsack = Knapsack(values, values, max_capacity)
        self.assertEqual(12, knapsack.get_expected_value())

    def test_walk_another_grid(self):
        max_capacity = 9
        values = [3, 4, 4, 4, 8]
        knapsack = Knapsack(values, values, max_capacity)
        self.assertEqual(9, knapsack.get_expected_value())
