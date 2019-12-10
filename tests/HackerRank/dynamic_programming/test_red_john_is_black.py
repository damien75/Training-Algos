from unittest import TestCase

from HackerRank.dynamic_programming.red_john_is_back import RedJohnIsBack


class RedJohnIsBackTest(TestCase):
    def setUp(self) -> None:
        self.instance = RedJohnIsBack()

    def test_get_nb_ways_organize_wall(self):
        self.assertEqual(0, self.instance.solve_red_john_is_back(1))
        self.assertEqual(3, self.instance.solve_red_john_is_back(7))
