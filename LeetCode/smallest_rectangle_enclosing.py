from typing import List, Tuple


class Enclosing:
    """
    Input : binary 2D grid of dimension n . m and location (i , j) of a value 1

    Goal: Return the area of the smallest rectangle enclosing all 1 values
    we can assume there is only 1 region to enclose and that this region is connected (no gaps)

    Idea: Since the region is connected, then:
       if a column i has a value 1 and column i-1 has no value 1, then the left border is i
       ==> therefore we will use a binary search starting from column i to find left and right border
           and a binary search starting from line j to find top and bottom borders

    complexity: O(n log m + m log n) in time and O(1) in space
    """

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def contains_value(self, m: int, in_row: bool) -> bool:
        if in_row:
            return 1 in self.grid[m]
        else:
            return 1 in [self.grid[i][m] for i in range(len(self.grid))]

    def search_left(self, i: int, j: int) -> int:
        while i <= j:
            m = (i + j) // 2
            if not self.contains_value(m, False):  # check if this column has a 1 value
                i = m + 1  # in that case the area is further right
            else:
                j = m - 1
        return i

    def search_right(self, i: int, j: int) -> int:
        while i <= j:
            m = (i + j) // 2
            if not self.contains_value(m, False):  # check if this column has a 1 value
                j = m - 1  # in that case the area is further left
            else:
                i = m + 1
        return j

    def search_top(self, i: int, j: int) -> int:
        while i <= j:
            m = (i + j) // 2
            if not self.contains_value(m, True):  # check if this column has a 1 value
                i = m + 1  # in that case the area is further down
            else:
                j = m - 1
        return i

    def search_bottom(self, i: int, j: int) -> int:
        while i <= j:
            m = (i + j) // 2
            if not self.contains_value(m, True):  # check if this column has a 1 value
                j = m - 1  # in that case the area is further up
            else:
                i = m + 1
        return j

    def smallest_area(self, start_point: Tuple[int, int]) -> int:
        i, j = start_point
        left = self.search_left(0, i)
        right = self.search_right(i + 1, len(self.grid[i]) - 1)
        top = self.search_top(0, j)
        bottom = self.search_bottom(j + 1, len(self.grid) - 1)
        return (bottom - top + 1) * (right - left + 1)
