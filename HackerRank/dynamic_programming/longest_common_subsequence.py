from typing import List, Any


class LongestCommonSubsequence(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / The Longest Common Subsequence

    Input: 2 arrays A and B

    Goal: find longest common subsequence

    Idea: keep track of the subsequences we have seen so far => LCS(i , j) will be
    the longest subsequence from A[0..i] and B[0..j]
    We define LCS(i , j) as follows:
    if i == 0 or j == 0: LCS(i , j) = 0
    elif A[i] == B[j]: LCS(i , j) = LCS(i - 1 , j - 1) + A[i]
    else: LCS(i , j) = max(LCS(i - 1 , j) , LCS(i , j - 1))
    """
    @staticmethod
    def longest(list_a: List[Any], list_b: List[Any]) -> List[int]:
        lcs: List[List[List[int]]] = [[[]] * (len(list_b) + 1) for _ in range(len(list_a) + 1)]

        for i in range(1, len(list_a) + 1):
            for j in range(1, len(list_b) + 1):
                if list_a[i - 1] == list_b[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + [list_a[i - 1]]
                else:
                    if len(lcs[i - 1][j]) > len(lcs[i][j - 1]):
                        lcs[i][j] = lcs[i - 1][j]
                    else:
                        lcs[i][j] = lcs[i][j - 1]
        return lcs[-1][-1]

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        _, _ = map(int, input().split())
        list_a = list(map(int, input().split()))
        list_b = list(map(int, input().split()))
        print(' '.join(str(el) for el in self.longest(list_a, list_b)))
