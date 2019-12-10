from typing import List


class GridSearch(object):
    """
    Source Hackerrank / Algorithms / Implementation / Grid Search

    Input: 2 grids: one small and one bigger

    Goal: Check if small grid is in the big one

    Idea: look for the first line of the small grid in the big one
    in that case get the index of the correspondance and check if the following lines match
    """

    @staticmethod
    def find_pattern_in_grid(big_grid: List[str], small_grid: List[str]) -> str:
        found = False
        for lineIndex in range(len(big_grid)):
            if small_grid[0] in big_grid[lineIndex]:
                start_index = big_grid[lineIndex].index(small_grid[0])
                curr_line = lineIndex
                found_here = True
                for line in small_grid[1:]:
                    curr_line += 1
                    if line not in big_grid[curr_line] or big_grid[curr_line].index(line) != start_index:
                        found_here = False
                        break
                if found_here:
                    return "YES"
            if found:
                break
        if not found:
            return "NO"

    @staticmethod
    def read_grid():
        n, m = map(int, input().split())
        grid = ["" for _ in range(n)]
        for i in range(n):
            grid[i] = input()
        return grid

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())
        for i in range(t):
            big_grid = self.read_grid()
            small_grid = self.read_grid()
            print(self.find_pattern_in_grid(big_grid, small_grid))
