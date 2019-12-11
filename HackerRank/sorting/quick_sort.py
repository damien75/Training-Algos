from typing import List


class QuickSort:
    """
    Source Hackerrank / Algorithms / Sorting / Quicksort In-Place

    Input: array of integers

    Goal: Return sorted array of integers, printing the array at each step of the partitioning method
    """

    def __init__(self, ar: List[int]):
        self.ar = ar

    def swap(self, i: int, j: int):
        temp = self.ar[i]
        self.ar[i] = self.ar[j]
        self.ar[j] = temp

    def partition(self, left: int, right: int) -> int:
        index = left
        for i in range(left, right - 1):
            if self.ar[i] <= self.ar[right - 1]:
                self.swap(i, index)
                index += 1
        self.swap(right - 1, index)
        return index

    def quick_sort(self, left: int, right: int):
        if right - left > 1:
            pos = self.partition(left, right)
            self.quick_sort(left, pos)
            self.quick_sort(pos + 1, right)

    def sorted(self) -> List[int]:
        self.quick_sort(0, len(self.ar))
        return self.ar

    def print_el(self, left: int, right: int):
        for i in range(left, right):
            print(self.ar[i], )

    @staticmethod
    def read_and_print_from_hackerrank():
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        _ = input()
        ar = [int(i) for i in input().strip().split()]
        s_ar = QuickSort(ar)
        s_ar.sorted()
        s_ar.print_el(0, len(ar))
