from unittest import TestCase

from LeetCode.abbreviate_word import Abbreviations


class AbbreviationsTest(TestCase):
    def setUp(self) -> None:
        words = ["deer", "door", "cake", "card"]
        self.instance = Abbreviations(words)

    def test_abbreviation_is_unique(self):
        self.assertFalse(self.instance.is_unique('dear'))
        self.assertTrue(self.instance.is_unique('cart'))
        self.assertFalse(self.instance.is_unique('cane'))
        self.assertTrue(self.instance.is_unique('make'))
