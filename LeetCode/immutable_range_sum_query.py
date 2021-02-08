from typing import List


class ImmutableRangeSum:
    """
    Input : array of integers

    Goal: Be able to compute the most efficiently possible the sum in a given range
    Indeed a lot of calls will be made to the sumRange function

    Idea: Store for every index the sum from all the way to the left until this index

    complexity: O(n) in time to store the sums and then constant lookup for each call to sumRange and O(n) in space
    """
    def __init__(self, ar: List[int]):
        self.leftSums = [0 for _ in range(len(ar))]
        self.leftSums[0] = ar[0]
        for i in range(1, len(ar)):
            self.leftSums[i] = self.leftSums[i - 1] + ar[i]

    def sum_range(self, i, j):
        if i <= 0:
            return self.leftSums[j]
        else:
            return self.leftSums[j] - self.leftSums[i - 1]
