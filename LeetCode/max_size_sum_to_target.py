from typing import List


class MaxSizeSumToTarget(object):
    """
    Input : integer array ar and integer k

    Goal: Find the maximum length of a subarray that sums to k.
    If there isn't one, return 0

    Idea: Use a hashtable with key: the sum from start to the current index and value: current index
    Then we do a single scan, left to right
    for i in range(len(ar)):
       tempSum += ar[i]
       if tempSum not in hashtable:
           hashtable[tempSum] = i
       if tempSum - k in hashtable: <-- in that case the sum from this index to the current index is k!!
           maxLength = max(maxLength , i - hashtable[tempSum - k])

    complexity: O(n) single scan in time and O(n) in space
    """
    @staticmethod
    def max_length_subarray_to_target(ar: List[int], target: int) -> int:
        temp_sum = 0
        max_length = 0
        h = {0 : -1}
        for i in range(len(ar)):
            temp_sum += ar[i]
            if temp_sum not in h:
                h[temp_sum] = i
            if temp_sum - target in h:
                max_length = max(max_length , i - h[temp_sum - target])
        return max_length
