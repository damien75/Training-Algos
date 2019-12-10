from typing import List


class MaximizeStock(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / Stock Maximize

    Input: evolution of a stock in time (1 <= time <= n) for t test cases

    Goal: compute the max profit we can make, we can either buy 1 share every time or sell all we have

    Idea: go in time from right to left
    m = 0 price at which we will sell the shares
    if the price[i] >= m then m = price[i] #in this case we will sell the preceding shares at this price, so we reset m
    profit += m - price[i]
    """
    @staticmethod
    def maximize_stock_retrospectively(time_span: int, price: List[int]) -> int:
        profit = 0
        m = 0
        for j in range(time_span - 1, -1, -1):
            if price[j] >= m:
                m = price[j]
            else:
                profit += m - price[j]
        return profit

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())
        for i in range(t):
            n = int(input())
            price = list(map(int, input().split()))
            print(self.maximize_stock_retrospectively(n, price))
