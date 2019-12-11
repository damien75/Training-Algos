import heapq
from typing import Tuple, List


class BurstBalloons(object):
    """
    Source: Careercup / Google / http://www.careercup.com/question?id=5719829237465088

    Input: array of size N with values
    if we burst balloon at position i, we add to the output values[i - 1]*values[i]*values[i + 1]
    And the value at position i is removed, values at positions i - 1 and i + 1 are now adjacent
    values all the way to the left and all the way to the right are 1, so that when the last balloon bursts
    the output will see its value increased by the value of the last balloon.

    Goal: burst balloons 1 by 1 to maximize the output

    Idea: look at all the local minimums, and burst the smallest one first, until we burst all the balloons
    """

    @staticmethod
    def find_best_maximum(values: List[int]) -> Tuple[int, int]:
        assert (len(values) > 3)
        if len(values) == 4:
            if values[1] > values[2]:
                return values[2], 2
            else:
                return values[1], 1
        maximum = []
        for i in range(1, len(values) - 1):
            heapq.heappush(maximum, (-values[i - 1] * values[i] * values[i + 1], i))
        return values[maximum[0][1]], maximum[0][1]

    def find_best_minimum(self, values: List[int]) -> Tuple[int, int]:
        assert (len(values) >= 3)
        if len(values) == 3:
            return values[1], 1
        else:
            minima = []
            for i in range(2, len(values) - 2):
                if values[i - 1] > values[i] and values[i + 1] > values[i]:
                    heapq.heappush(minima, (values[i], i))
            if len(minima) == 0:
                return self.find_best_maximum(values)
            else:
                return minima[0]

    def maximize_value_collected(self, values: List[int]) -> int:
        values = [1] + values
        values.append(1)  # add 1 on both extremities
        output = 0
        while len(values) > 2:
            best_minima, i = self.find_best_minimum(values)
            output += values[i - 1] * best_minima * values[i + 1]
            values.pop(i)
        return output
