from unittest import TestCase

from LeetCode.find_duplicate import DuplicateFinder


class DuplicateFinderTest(TestCase):
    def setUp(self) -> None:
        self.instance = DuplicateFinder()

    def test_find_duplicates(self):
        """
        step 1:
        slow => 1 , fast => 2
        step 2:
        slow => 2 , fast => 4
        step 3:
        slow => 3 , fast => 6
        step 4:
        slow => 4 , fast => 8
        step 5:
        slow => 5 , fast => 10
        step 6:
        slow => 6 , fast => 12
        step 7:
        slow => 7 , fast => 9
        step 8:
        slow => 8 , fast => 11
        step 9:
        slow => 9 , fast => 8
        step 10:
        slow => 10 , fast => 10 <-- they meet, but not necessarily at the entry of the loop

        Say slow has done k steps and fast 2k, and the entry of the cycle was at distance n
        During the second loop, suppose find does k steps,
        then slow will have done 2k steps and they have to meet again, as before
        They were both moving at the same speed, so if they met before we would have stopped,
        and that would have been the entry, else if they meet only at 2k then this is the entry point
        """
        self.assertEqual(8, self.instance.find_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 8]))
