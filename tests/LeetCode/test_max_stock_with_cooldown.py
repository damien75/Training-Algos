from unittest import TestCase

from LeetCode.max_stock_with_cooldown import MaxStock


class MaxStockTest(TestCase):
    def setUp(self) -> None:
        self.instance = MaxStock()

    def test_max_stock_with_cooldown(self):
        """
        transactions = [buy, sell, cooldown, buy, sell]
        """
        prices = [1, 2, 3, 0, 2]
        self.assertEqual(3, self.instance.max_profit(prices))
