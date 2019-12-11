from functools import reduce
from typing import Set, List, Callable


class PowerSet(object):
    """
    Source: Rosetta code
    """
    @staticmethod
    def list_powerset(lst: List[int]):
        # the power set of the empty set has one element, the empty set
        result = [[]]
        for x in lst:
            # for every additional element in our set
            # the power set consists of the subsets that don't
            # contain this element (just take the previous power set)
            # plus the subsets that do contain the element (use list
            # comprehension to add [x] onto everything in the
            # previous power set)
            result.extend([subset + [x] for subset in result])
        return result

    # the above function in one statement
    @staticmethod
    def list_powerset2(lst: List[int]):
        return reduce(lambda result, x: result + [subset + [x] for subset in result],
                      lst, [[]])

    def powerset(self, s: Set[int], func_list_powerset: Callable[[List[int]], List[List[int]]]) -> List[Set[int]]:
        return list(map(set, func_list_powerset(list(s))))
