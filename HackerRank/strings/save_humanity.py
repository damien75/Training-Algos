from typing import List


class BinarySearchDifferenceBetweenString(object):
    """
    Source Hackerrank / Algorithms / Strings / Save Humanity

    Input: 2 strings

    Goal: Check if a substring of the 1st string can have at most 1 difference with 2nd string

    Idea: do a binary search to look for the potential 1 difference between the strings

    complexity: O(n log(n))
    """

    @staticmethod
    def binary_search_are_similar(s: str, t: str) -> bool:
        assert (len(s) == len(t))
        if s == t:
            return True
        else:
            left = 0
            right = len(s)
            while left <= right:
                m = (left + right) // 2
                left_similar = s[left:m] == t[left:m]
                right_similar = s[m + 1:right] == t[m + 1:right]
                middle_similar = s[m] == t[m]
                if left_similar and right_similar:
                    return True
                elif left_similar and middle_similar:
                    left = m + 1
                elif right_similar and middle_similar:
                    right = m
                else:
                    return False

    def find_similarities(self, p: str, v: str) -> List[int]:
        """
        :return: List of indices with similarities
        """
        indices = []
        for j in range(len(p) - len(v) + 1):
            if self.binary_search_are_similar(p[j: j + len(v)], v):
                indices.append(j)
        return indices

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())
        for i in range(t):
            p, v = input().split()
            match = False
            indices = []
            for j in range(len(p) - len(v) + 1):
                if self.binary_search_are_similar(p[j: j + len(v)], v):
                    match = True
                    indices.append(j)
            if match:
                for j in indices:
                    print(j,)
            else:
                print('No Match!')
