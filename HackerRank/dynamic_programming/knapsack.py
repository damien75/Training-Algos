from typing import List


class Knapsack:
    """
    source Hackerrank / Algorithms / Dynamic Programming / Knapsack

    Input: max capacity W, and int values

    Goal: compute the max sum not exceeding W using only elements in the given list

    Idea: when W = 0 => expected value = 0
    when len(values) = 0 => expected value = 0
    for cap w and first i values:
       if values[i] <= cap:
           expectedValue = max(expectedValue[i - 1][cap] , expectedValue[i][cap - values[i]] + values[i])
    """
    def __init__(self, values: List[int], weights: List[int], max_capacity: int):
        self.array = []
        self.values = values
        self.weights = weights
        self.max_capacity = max_capacity

    def get_expected_value(self) -> int:
        for i in range(len(self.values) + 1):  # add 0 when capacity is equal to 0
            self.array.append([0])
        for i in range(1, self.max_capacity + 1):  # add 0 when there are no available values
            self.array[0].append(0)

        for i in range(1, len(self.values) + 1):
            j = i - 1
            for cap in range(1, self.max_capacity + 1):
                if self.values[j] > cap:
                    self.array[i].append(self.array[i - 1][cap])
                else:
                    self.array[i].append(max(self.array[i - 1][cap],
                                             self.array[i][cap - self.weights[j]] + self.values[j]))
        return self.array[-1][-1]

    @staticmethod
    def read_and_print_from_hackerrank():
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())

        for _ in range(t):
            n, max_capacity = map(int, input().split())
            values = list(map(int, input().split()))
            knap = Knapsack(values, values, max_capacity)
            print(knap.get_expected_value())
