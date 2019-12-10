from logging import getLogger
from os import environ
from os.path import dirname, join, realpath
from time import time
from unittest import TestCase, skipUnless

from HackerRank.search.max_mod_sum import MaxModuloSum


@skipUnless(environ.get('RUN_EXPENSIVE_TESTS') is not None, 'this test takes around 2s')
class MaxModuloSumTest(TestCase):
    def setUp(self) -> None:
        self.instance = MaxModuloSum()
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')

    def test_max_mod_sum(self):
        start = time()
        resources_path = join(realpath(dirname(dirname(dirname(__file__)))), 'resources')
        result = self.instance.solve_from_custom_input(join(resources_path, 'maxSum test1.txt'))
        with open(join(resources_path, 'maxSum output1.txt')) as f:
            success = True
            for i in range(len(result)):
                success &= int(f.readline()) == result[i]
        self.assertEqual(True, success)
        self.logger.info(f'Execution time(s): {time() - start}')
