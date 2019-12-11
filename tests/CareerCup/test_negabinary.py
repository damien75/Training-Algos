from unittest import TestCase

from CareerCup.negabinary import NegaBinary


class NegaBinaryTest(TestCase):
    def setUp(self) -> None:
        self.instance = NegaBinary()

    def test_get_negabinary(self):
        self.assertEqual('110001', self.instance.negative_binary(-15))
        self.assertEqual('110', self.instance.negative_binary(2))
        self.assertEqual('11101', self.instance.negative_binary(13))
