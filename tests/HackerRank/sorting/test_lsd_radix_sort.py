from logging import getLogger
from os import environ
from random import randint
from time import time
from unittest import TestCase, skipUnless

from HackerRank.sorting.lsd_radix_sort import RadixSort
from HackerRank.sorting.quick_sort import QuickSort


@skipUnless(environ.get('RUN_EXPENSIVE_TESTS') is not None, 'this test takes around 70s')
class RadixSortTest(TestCase):
    def setUp(self) -> None:
        self.a = [randint(0, 10000) for _ in range(1000000)]
        self.radix_sort_instance = RadixSort()
        self.quick_sort_instance = QuickSort(self.a)
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')

    def test_radix_sort_accuracy(self):
        self.assertEqual([1, 2, 3, 5, 7, 8, 9], self.radix_sort_instance.radix_sort([1, 3, 9, 8, 2, 7, 5], 10, 7))

    def test_radix_sort_speed_vs_quick_sort(self):
        start_radix = time()
        radix_sorted = self.radix_sort_instance.radix_sort(self.a, 10, 5)
        self.logger.info(f'Execution time(s) for Radix Sort: {time() - start_radix}')

        start_quick_sort = time()
        quick_sorted = self.quick_sort_instance.sorted()
        self.logger.info(f'Execution time(s) for Quick Sort: {time() - start_quick_sort}')

        self.assertEqual(quick_sorted, radix_sorted)
