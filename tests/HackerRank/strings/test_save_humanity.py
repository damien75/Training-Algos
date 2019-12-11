from unittest import TestCase

from HackerRank.strings.save_humanity import BinarySearchDifferenceBetweenString


class BinarySearchDifferenceBetweenStringTest(TestCase):
    def setUp(self) -> None:
        self.instance = BinarySearchDifferenceBetweenString()

    def test_find_similarities(self):
        self.assertEqual([1, 2], self.instance.find_similarities('abbab', 'ba'))
        self.assertEqual([], self.instance.find_similarities('hello', 'world'))
        self.assertEqual([0, 2], self.instance.find_similarities('banana', 'nan'))
