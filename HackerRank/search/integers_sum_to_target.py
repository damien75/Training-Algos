from typing import List, Tuple


class SumToTarget(object):
    @staticmethod
    def get_sets_of_three_that_sum_to_target(ar: List[int], t: int) -> List[Tuple[int, int, int]]:
        """
        Input: integer array

        Goal: output all sets of 3 values that sum up to target t, ie n1 + n2 + n3 = t

        Idea: complexity O(n^2)
        1st: sort the array
        for each element in the array:
           tempTarget = t - currElement
           have 2 pointers left and right with left initially = currPos + 1 and right len(ar) - 1
           while left < right:
               tempSum = left + right
               if sum < tempTarget:
                   left += 1
               elif sum > tempTarget:
                   right -= 1
               else:
                   results.append((currElement , left , right))
        """
        ar.sort()
        results = []
        for i in range(len(ar) - 2):
            temp_target = t - ar[i]
            left = i + 1
            right = len(ar) - 1
            while left < right:
                temp_sum = ar[left] + ar[right]
                if temp_sum < temp_target:
                    left += 1
                elif temp_sum > temp_target:
                    right -= 1
                else:
                    results.append((ar[i] , ar[left] , ar[right]))
                    left += 1
                    right -= 1
        return results

    @staticmethod
    def get_sets_of_two_that_sum_to_target(ar: List[int], t: int) -> List[Tuple[int, int]]:
        """
        Goal: output all sets of 2 values that sum up to target t, ie n1 + n2 = t

        Idea: complexity O(n)
        for each element in the array:
           store the element in a set (or hashtable)
        for each element in the array:
           look up if t - element is in the hashtable
           if so:
               results.append((element , t - element))
        """
        s = set()
        results = []
        for el in ar:
            s.add(el)
        for el in ar:
            if t - el in s:
                results.append((el , t - el))
        return results
