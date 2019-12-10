import sys
from typing import List


class CoinOnTheTable(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / Coin on the Table

    Input: grid of size n x m with instructions and a goal

    Goal: reach the goal with time t <= k, changing as few instructions on grid as possible

    Idea: see in the grid in how many moves t we can get to a given point, while t <= k
    case 1: we can reach the goal with t <= k --> output 0
    case 2: start from * and see in how many moves we can get to their neighbors,
    if for one of them we can get there with moves <
    """
    @staticmethod
    def nb_changes_for_solution(grid: List[List[str]], n: int, m: int, k: int,
                                i_destination: int, j_destination: int) -> int:
        from_dir = [(0, 1, 'L'), (0, -1, 'R'), (-1, 0, 'D'), (1, 0, 'U')]
        f = [[[sys.maxsize for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
        # f will count the modifications
        for i in range(k + 1):
            f[0][0][i] = 0  # 0 steps needed to get there

        for line in range(1, k + 1):
            for i in range(n):
                for j in range(m):
                    # our current position
                    for direction in from_dir:
                        # direction is where we can come from
                        i_from = i + direction[0]
                        j_from = j + direction[1]
                        if 0 <= i_from < n and 0 <= j_from < m:
                            if grid[i_from][j_from] == direction[2]:
                                # if the direction was pointing to us, then pick the best
                                f[i][j][line] = min(f[i][j][line], f[i_from][j_from][line - 1])
                                # no modification in this case
                            else:
                                f[i][j][line] = min(f[i][j][line], f[i_from][j_from][line - 1] + 1)
                                # modification so +1 here

        mini = sys.maxsize

        for line in range(k + 1):
            mini = min(mini, f[i_destination][j_destination][line])
        return mini if mini != sys.maxsize else -1

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        n, m, k = map(int, input().split())
        grid = []
        for i in range(n):
            line = list(map(int, input().split()))
            if '*' in line:
                i_destination = i
                j_destination = line.index('*')
            grid.append(line)
        print(self.nb_changes_for_solution(grid, n, m, k, i_destination, j_destination))
