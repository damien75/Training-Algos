from typing import List


class DuplicateFinder(object):
    """
    Input : integer array of length n + 1 containing integers in range(n)

    Goal: Find the duplicate

    Idea: Run a first time 2 pointers with different speed until they meet in the cycle,
    then run again with same speed so that they meet at the beginning of the cycle

    complexity: O(n) in time and O(1) in space!!!
    """
    @staticmethod
    def find_duplicate(ar: List[int]) -> int:
        fast = slow = find = 0
        slow = ar[slow]
        fast = ar[ar[fast]]
        while fast != slow:  # First loop
            slow = ar[slow]
            fast = ar[ar[fast]]
        while find != slow:  # Second loop
            find = ar[find]
            slow = ar[slow]
        return find
