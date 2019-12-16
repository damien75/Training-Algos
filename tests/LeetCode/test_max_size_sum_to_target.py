from unittest import TestCase

from LeetCode.max_size_sum_to_target import MaxSizeSumToTarget


class MaxSizeSumToTargetTest(TestCase):
    def setUp(self) -> None:
        self.instance = MaxSizeSumToTarget()

    def test_sum_to_target_1(self):
        """
        expect to return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
        """
        ar1 = [1, -1, 5, -2, 3]
        k1 = 3
        self.assertEqual(4, self.instance.max_length_subarray_to_target(ar1, k1))

    def test_sum_to_target_2(self):
        """
        expect to return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
        """
        ar2 = [-2, -1, 2, 1]
        k2 = 1
        self.assertEqual(2, self.instance.max_length_subarray_to_target(ar2, k2))
