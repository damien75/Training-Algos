from unittest import TestCase

from HackerRank.dynamic_programming.maximize_stock import MaximizeStock


class MaximizeStockTest(TestCase):
    def setUp(self) -> None:
        self.instance = MaximizeStock()

    def test_maximize_retrospectively_time_span_1(self):
        self.assertEqual(0, self.instance.maximize_stock_retrospectively(3, [5, 3, 2]))

    def test_maximize_retrospectively_time_span_2(self):
        self.assertEqual(197, self.instance.maximize_stock_retrospectively(3, [1, 2, 100]))

    def test_maximize_retrospectively_time_span_3(self):
        self.assertEqual(3, self.instance.maximize_stock_retrospectively(4, [1, 3, 1, 2]))
