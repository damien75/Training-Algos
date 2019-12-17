from unittest import TestCase

from interviews.celebrity_graph import CelebrityGraph


class CelebrityGraphTest(TestCase):
    def test_celebrity_finder1(self):
        """
        This is an example test case where we have set it up such that
        person 2 is the celebrity.
        """
        def knows2(i, j):
            if i == j:  # you know yourself
                return True
            if j == 2:  # everyone knows person 2
                return True
            return False  # by default don't know anyone other than person 2

        self.assertEqual(2, CelebrityGraph(4, knows2).find_celeb())

    def test_celebrity_finder2(self):
        """
        Another test case where people only know themselves, so no celeb exists
        """
        def knows_self(i, j):
            return i == j

        self.assertIsNone(CelebrityGraph(4, knows_self).find_celeb())
