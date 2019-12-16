from unittest import TestCase

from LeetCode.word_pattern import PatternRecognition


class PatternRecognitionTest(TestCase):
    def test_pattern_1(self):
        rec = PatternRecognition('abab', 'redblueredblue')
        self.assertTrue(rec.word_follows_pattern())

    def test_pattern_2(self):
        rec = PatternRecognition('aaaa', 'asdasdasdasd')
        self.assertTrue(rec.word_follows_pattern())

    def test_pattern_3(self):
        rec = PatternRecognition('aabb', 'xyzabcxzyabc')
        self.assertFalse(rec.word_follows_pattern())
