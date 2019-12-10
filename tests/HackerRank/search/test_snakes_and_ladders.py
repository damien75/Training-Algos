from logging import getLogger
from os.path import dirname, realpath, join
from time import time
from unittest import TestCase

from HackerRank.search.snakes_and_ladders import SnakesAndLadders


class SnakesAndLaddersTest(TestCase):
    def setUp(self) -> None:
        self.instance = SnakesAndLadders()
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')
        self.resources_dir = join(realpath(dirname(dirname(dirname(__file__)))), 'resources')
        self.top = 100

    def get_min_nb_of_toss_from_file(self, input_file: str, output_file: str):
        start = time()
        results = []
        with open(join(self.resources_dir, input_file)) as f:
            t = int(f.readline())
            for _ in range(t):
                n = int(f.readline())
                jumps = [i for i in range(self.top + 8)]
                for _ in range(n):
                    s, e = map(int, f.readline().split())
                    jumps[s] = e
                m = int(f.readline())
                for _ in range(m):
                    s, e = map(int, f.readline().split())
                    jumps[s] = e
                results.append(self.instance.min_number_of_toss(jumps, self.top))

        self.logger.info(f'Execution time(s): {time() - start}')
        with open(join(self.resources_dir, output_file)) as f:
            success = True
            for i in range(len(results)):
                success &= int(f.readline()) == results[i]
        self.assertEqual(True, success)

    def test_get_min_nb_of_toss_snakes1(self):
        self.get_min_nb_of_toss_from_file('snakesInput.txt', 'snakesOutput.txt')

    def test_get_min_nb_of_toss_snakes2(self):
        self.get_min_nb_of_toss_from_file('snakesInput2.txt', 'snakesOutput2.txt')
