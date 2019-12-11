from logging import getLogger
from os import environ
from time import time
from unittest import TestCase, skipUnless

from CareerCup.sum_of_elements_to_target import SubsetToTarget


@skipUnless(environ.get('RUN_EXPENSIVE_TESTS') is not None, 'this test takes around 15s')
class SubsetToTargetTest(TestCase):
    def setUp(self) -> None:
        self.instance = SubsetToTarget(SubsetToTarget.US_POPULATION)
        self.logger = getLogger(f'{__name__}.{__class__.__qualname__}')

    def test_subset(self):
        start = time()
        solution = self.instance.solve_with_stack(0, [0] * len(self.instance.data), 0, self.instance.TARGET)
        self.logger.info(f'Solution found in {time() - start}')
        self.assertEqual(True, solution)
