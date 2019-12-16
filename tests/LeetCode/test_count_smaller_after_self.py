from unittest import TestCase

from LeetCode.count_smaller_after_self import SmallerElements


class SmallerElementsTest(TestCase):
    def setUp(self) -> None:
        self.instance = SmallerElements()

    def test_count_smaller_elements(self):
        """
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.
        """
        ar = [5, 2, 6, 1]

        self.assertListEqual([2, 1, 1, 0], self.instance.count_smaller_elements(ar))
