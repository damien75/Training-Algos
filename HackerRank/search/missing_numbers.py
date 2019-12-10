from typing import List, Any


class MissingNumbers(object):
    """
    Source Hackerrank / Algorithms / Search / Missing Numbers

    Input: arrays A and B containing number in a 100 range

    Goal: return the numbers that are not present the same number of times in both arrays

    Idea: go through array A, store every number in a hashtable to count them, then dicrease while going through B
    complexity linear in the length of the array
    """
    @staticmethod
    def show_missing_numbers(array_a: List[Any], array_b: List[Any]) -> List[Any]:
        count = {}
        for u in array_a:
            if u in count:
                count[u] += 1
            else:
                count[u] = 1

        for v in array_b:
            if v in count:
                count[v] -= 1
            else:
                count[v] = -1

        missing_nb = []
        for u in count:
            if count[u] != 0:
                missing_nb.append(u)

        return missing_nb

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        for el in self.show_missing_numbers(a, b):
            print(el,)
