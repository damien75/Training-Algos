from typing import Any, List


class LongestIncreasingSubsequence(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / The Longest Increasing Subsequence

    Input: sequence of integers of size n

    Goal: find the length of the longest subsequence of increasing integers in this array

    Idea: solution in O(n log n) time complexity
    go through the array in normal path, from left to right
    when we see a new element a[i]:
    a[i] is smaller than all other last elements of the list we have so far => create new list of size 1 with a[i] as
    last element and remove other list of size 1
    a[i] is bigger than all others => add it to the list of longest length so far
    a[i] is between smallest and biggest => add it to the list where its end element is smallest and it's bigger than
    a[i] and remove all lists of same length
    """
    @staticmethod
    def find_position(ar: List[Any], el: Any) -> int:
        left = -1
        right = len(ar) - 1
        while right > left + 1:
            m = (left + right) // 2
            if ar[m] >= el:
                right = m
            else:
                left = m
        return right

    def length_of_longest_subsequence(self, ar: List[Any]) -> int:
        if len(ar) == 0:
            return 0
        else:
            last_element = [ar[0]]
            best_length = 1
            for i in range(1, len(ar)):
                if ar[i] < last_element[0]:
                    last_element[0] = ar[i]
                elif ar[i] > last_element[best_length - 1]:
                    best_length += 1
                    last_element.append(ar[i])
                else:
                    last_element[self.find_position(last_element, ar[i])] = ar[i]
            return best_length

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        n = int(input())
        a = [0] * n
        for i in range(n):
            a[i] = int(input())
        print(self.length_of_longest_subsequence(a))
