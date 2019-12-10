from unittest import TestCase

from HackerRank.dynamic_programming.candies import MinimumNumberOfCandies


class CandiesTest(TestCase):
    def setUp(self) -> None:
        self.n_students = 3
        self.grades = [1, 2, 2]
        self.instance = MinimumNumberOfCandies()

    def test_min_nb_candies_to_buy(self):
        self.assertEqual(4, self.instance.min_nb_candies(self.n_students, self.grades))
