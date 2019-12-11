from unittest import TestCase

from CareerCup.power_set import PowerSet


class PowerSetTest(TestCase):
    def setUp(self) -> None:
        self.instance = PowerSet()

    def test_get_negabinary(self):
        self.assertListEqual(
            [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {4}, {1, 4}, {2, 4}, {1, 2, 4}, {3, 4}, {1, 3, 4},
             {2, 3, 4}, {1, 2, 3, 4}], self.instance.powerset({1, 2, 3, 4}, self.instance.list_powerset))
        self.assertListEqual(
            [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {4}, {1, 4}, {2, 4}, {1, 2, 4}, {3, 4}, {1, 3, 4},
             {2, 3, 4}, {1, 2, 3, 4}], self.instance.powerset({1, 2, 3, 4}, self.instance.list_powerset2))
