from typing import Any, List


class BiggerIsGreater(object):
    """
    Source Hackerrank / Algorithms / Sorting / Bigger is Greater

    Input : string s

    Goal: from this string, reorganize character to have the smallest lexicographically greater string than s
    i.e. we need to switch letters as far on the right as possible

    Idea: look at possible indices where we could swap the letters
    if we can, then do it and return the string with right part sorted
    """

    @staticmethod
    def swap(tab: List[Any], i1: int, i2: int):
        temp = tab[i1]
        tab[i1] = tab[i2]
        tab[i2] = temp

    def next_string(self, s: str) -> str:
        s = list(s)
        left = len(s) - 2
        while left >= 0:
            right = len(s) - 1
            while right > left:
                if s[left] < s[right]:
                    self.swap(s, left, right)
                    s[left + 1:] = sorted(s[left + 1:])  # need to sort the rest of the string to get the smallest
                    return "".join(s)
                right -= 1
            left -= 1
        return "no answer"

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())
        for _ in range(t):
            s = input()
            print(self.next_string(s))
