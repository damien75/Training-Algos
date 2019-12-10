from unittest import TestCase

from HackerRank.search.grid_search import GridSearch


class GridSearchTest(TestCase):
    def setUp(self) -> None:
        self.instance = GridSearch()

    def test_search_grid1(self):
        big_grid = ["7283455864",
                    "6731158619",
                    "8988242643",
                    "3830589324",
                    "2229505813",
                    "5633845374",
                    "6473530293",
                    "7053106601",
                    "0834282956",
                    "4607924137"]
        small_grid = ["9505",
                      "3845",
                      "3530"]
        self.assertEqual('YES', self.instance.find_pattern_in_grid(big_grid, small_grid))

    def test_search_grid2(self):
        big_grid = ["400453592126560",
                    "114213133098692",
                    "474386082879648",
                    "522356951189169",
                    "887109450487496",
                    "252802633388782",
                    "502771484966748",
                    "075975207693780",
                    "511799789562806",
                    "404007454272504",
                    "549043809916080",
                    "962410809534811",
                    "445893523733475",
                    "768705303214174",
                    "650629270887160"]
        small_grid = ["99", "99"]
        self.assertEqual('NO', self.instance.find_pattern_in_grid(big_grid, small_grid))
