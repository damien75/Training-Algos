from logging import getLogger
from unittest import TestCase

from HackerRank.sorting.quick_sort import QuickSort


class QuickSortTest(TestCase):
    def setUp(self) -> None:
        self.instance = QuickSort([1, 3, 9, 8, 2, 7, 5])
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')

    def test_quicksort_accuracy(self):
        self.assertEqual([1, 2, 3, 5, 7, 8, 9], self.instance.sorted())
