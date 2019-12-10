import os


class PalindromeSubsequences(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / Play with words

    Input: string of length n

    Goal: find the max possible product of length of 2 non overlapping palindrome subsequence in string

    illustration with example: eeegeeksforskeeggeeks
    A possible optimal solution is eee-g-ee-ksfor-skeeggeeks being eeeee the one subsequence and skeeggeeks the other
    one.
    We can also select eegee in place of eeeee, as both have the same length.

    Idea: solution in O(n log n) time complexity
    Let L[0, n - 1] be the longest palindrome subsequence of the substring s[0 : n - 1]
    if s[0] == s[n - 1]:
      L[0, n - 1] = 2 + L[1, n - 2]
    else:
      L[0, n - 1] = max(L[1, n - 1], L[0, n - 2])
    Finally the result is max(L[0, i] * L[i + 1, n - 1]) for i in [0, n - 1]
    """
    @staticmethod
    def play_with_words(s: str) -> int:
        n = len(s)
        longest_palindrome_subsequencce = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            longest_palindrome_subsequencce[i][i] = 1
        for cl in range(2, n+1):
            for i in range(n-cl+1):
                j = i+cl-1
                if s[i] == s[j] and cl == 2:
                    longest_palindrome_subsequencce[i][j] = 2
                elif s[i] == s[j]:
                    longest_palindrome_subsequencce[i][j] = longest_palindrome_subsequencce[i+1][j-1] + 2
                else:
                    longest_palindrome_subsequencce[i][j] = max(longest_palindrome_subsequencce[i][j-1],
                                                                longest_palindrome_subsequencce[i+1][j])

        max_prod = 0
        for i in range(1, n - 1):
            max_prod = max(max_prod,
                           longest_palindrome_subsequencce[0][i] * longest_palindrome_subsequencce[i + 1][n - 1])

        return max_prod

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        with open(os.environ['OUTPUT_PATH'], 'w') as output_file:
            s = input()
            result = self.play_with_words(s)
            output_file.write(str(result) + '\n')
