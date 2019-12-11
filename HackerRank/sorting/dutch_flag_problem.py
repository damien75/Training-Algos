from typing import List, Any


class DutchFlag(object):
    """
    Input: integer array, int low, int high

    Goal: put all values lower than low on left, all values higher than high on right, in a single pass

    Idea: have 2 pointers for the left and right limits and one pointer looking at
    elements not yet seen in the middle
    """

    @staticmethod
    def swap(ar: List[Any], i: int, j: int):
        temp = ar[i]
        ar[i] = ar[j]
        ar[j] = temp

    def partition(self, ar: List[int], low: int, high: int) -> List[int]:
        left, right = 0, len(ar) - 1
        mid = left
        while mid <= right:
            if ar[mid] < low:
                self.swap(ar, mid, left)
                mid += 1
                left += 1
            elif ar[mid] > high:
                self.swap(ar, mid, right)
                right -= 1
            else:
                mid += 1
        return ar
