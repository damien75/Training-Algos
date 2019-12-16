from unittest import TestCase

from LeetCode.duplicate_letters import DuplicateLetters


class DuplicateLettersTest(TestCase):
    def setUp(self) -> None:
        self.instance = DuplicateLetters()

    def test_remove_duplicates(self):
        self.assertEqual('bac', self.instance.remove_duplicate_letters_from('bcac'))
        self.assertEqual('acdb', self.instance.remove_duplicate_letters_from('cbacdcbc'))
