from typing import List


class RadixSort(object):
    """
    Faster way to sort m-bit integers, if m small
    n = len(array)
    The complexity will be O(m*n)

    Idea: we sort for each pass of x in range(maxLen), the int by its least significant digit

    originalList = [170, 45, 75, 90, 802, 2, 24, 66]

    After 1st path:

    bins = [[170 , 90] , [] , [802 , 2] , [] , [24] , [45 , 75] , [66] , [] , [] , []]

    then the queue:

    queue = [170 , 90 , 802 , 2 , 24 , 45 , 75 , 66]

    After 2nd path:

    bins = [[802 , 2] , [] , [24] , [] , [45] , [] , [66] , [170 , 75] , [] , [90]]

    then the queue:

    queue = [802 , 2 , 24 , 45 , 66 , 170 , 75 , 90]

    After 3rd path:

    bins = [[2 , 24 , 45 , 66 , 75] , [170] , [] , [] , [] , [] , [] , [] , [802] , []]

    then the queue:

    queue = [2 , 24 , 45 , 66 , 75 , 170 , 802]
    """
    @staticmethod
    def radix_sort(original_list: List[int], n: int, max_len: int) -> List[int]:
        queue = original_list
        for x in range(max_len):
            bins = [[] for _ in range(n)]
            for y in queue:
                bins[(y // 10 ** x) % n].append(y)
            queue = []
            for section in bins:
                queue.extend(section)
        return queue
