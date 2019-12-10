from unittest import TestCase

from HackerRank.search.missing_numbers import MissingNumbers


class MissingNumbersTest(TestCase):
    def setUp(self) -> None:
        self.instance = MissingNumbers()

    def test_get_missing_numbers(self):
        self.assertEqual([204, 205, 206], self.instance.show_missing_numbers(
            [203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
            [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]))
