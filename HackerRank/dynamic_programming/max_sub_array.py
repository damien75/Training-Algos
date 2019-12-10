from typing import Tuple, List


class MaxSubArray(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / The Maximum Subarray

    Input: unsorted array

    Goal: compute max sum of uncontiguous and contiguous el in array

    Idea: for case where all elements < 0, return the max of the array for both
    else, for the uncontiguous sum, return the sum of positive numbers

    for the contiguous sum, suppose we have the best sum so far, there are 2 cases:
    1) adding an element will keep our sum > 0, so we add it to the sum
    2) adding an element will make our sum < 0, so we start again from the next position with currSum = 0
    """
    @staticmethod
    def compute_best_sum(a: List[int]) -> Tuple[int, int]:
        un_contigu_sum = sum(filter(lambda el: el > 0, a))
        if un_contigu_sum == 0:
            return max(a), max(a)
        else:
            contigu_sum = 0
            curr_sum = 0
            for x in a:
                curr_sum = max(0, curr_sum + x)
                contigu_sum = max(contigu_sum, curr_sum)
            return contigu_sum, un_contigu_sum

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())

        for i in range(t):
            _ = input()
            a = list(map(int, input().split()))
            print(self.compute_best_sum(a))
