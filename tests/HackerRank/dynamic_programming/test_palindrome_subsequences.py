from unittest import TestCase

from HackerRank.dynamic_programming.palindrome_subsequences import PalindromeSubsequences


class PalindromeSubsequencesTest(TestCase):
    def setUp(self) -> None:
        self.instance = PalindromeSubsequences()

    def test_get_max_product(self):
        self.assertEqual(50, self.instance.play_with_words('eeegeeksforskeeggeeks'))
