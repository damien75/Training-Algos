from unittest import TestCase

from CareerCup.concatenation_in_set import ConcatenationInSet


class ConcatenationInSetTest(TestCase):
    def setUp(self) -> None:
        self.instance = ConcatenationInSet()

    def test_word_can_be_built(self):
        s = {"world", "hello", "super", "hell"}
        self.assertTrue(self.instance.check_if_word_can_be_obtained_from_key_concatenation(s, 'helloworld'))
        self.assertFalse(self.instance.check_if_word_can_be_obtained_from_key_concatenation(s, 'superman'))
        self.assertTrue(self.instance.check_if_word_can_be_obtained_from_key_concatenation(s, 'hellohello'))
