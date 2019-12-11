from unittest import TestCase

from HackerRank.sorting.bigger_is_greater import BiggerIsGreater


class BiggerIsGreaterTest(TestCase):
    def setUp(self) -> None:
        self.instance = BiggerIsGreater()

    def test_get_smallest_lexicographically_greater_string(self):
        self.assertEqual('ba', self.instance.next_string('ab'))
        self.assertEqual('no answer', self.instance.next_string('bb'))
        self.assertEqual('hegf', self.instance.next_string('hefg'))
        self.assertEqual('dhkc', self.instance.next_string('dhck'))
        self.assertEqual('hcdk', self.instance.next_string('dkhc'))
