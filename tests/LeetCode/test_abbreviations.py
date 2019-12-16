from unittest import TestCase

from LeetCode.abbreviation import Abbreviations


class AbbreviationsTest(TestCase):
    def setUp(self) -> None:
        word = "word"
        self.instance = Abbreviations(word)

    def test_abbreviation_is_unique(self):
        self.assertListEqual(['4', '3d', '2r1', '2rd', '1o2', '1o1d', '1or1', '1ord', 'w3', 'w2d', 'w1r1', 'w1rd',
                              'wo2', 'wo1d', 'wor1', 'word'], self.instance.get_all_abbreviations(0, '', 0))
