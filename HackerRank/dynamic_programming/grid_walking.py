from typing import List


class GridWaling(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / Grid Walking

    Input: n dimensional grid , integer m

    Goal: find the nb of ways you can take m steps without leaving grid. Each step can be taken
    forward or backward in any direction

    Idea: to get to value v using i coins = A[i - 1][v] + A[i][v - v_i] if v_i <= v
    else: = A[i - 1][v]
    """
    MOD = 1000000007

    @staticmethod
    def choose(n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        else:
            p, q = 1, 1
            for i in range(1, min(k, n - k) + 1):
                p *= n
                q *= i
                n -= 1
            return p // q

    @staticmethod
    def count_ways(dimensions: int, steps: int, path_length: List[int]) -> List[List[List[int]]]:
        """
        Find all possible ways for all points and steps
        The first dimension is the number of dimensions n
        The second dimension is the number of steps 1..M
        The third dimension is the length of the path in this dimension
        """
        ways = [[[0] * path_length[i] for _ in range(steps + 1)] for i in range(dimensions)]

        for i in range(dimensions):  # ie for each dimension
            # Initial counting of zeroth and first steps
            for j in range(path_length[i]):  # ie for each step we can take in this direction
                ways[i][0][j] = 1  # only 1 way if M = 0

                if j > 0:
                    ways[i][1][j] += 1  # 2 ways if we're not on the edge
                if j < path_length[i] - 1:
                    ways[i][1][j] += 1

            # Higher steps
            for s in range(2, steps + 1):
                for j in range(path_length[i]):
                    # for s > 1, then the #ways is sum of the number of ways to get to each neighbor with s-1 steps
                    if j > 0:
                        ways[i][s][j] += ways[i][s - 1][j - 1]
                    if j < path_length[i] - 1:
                        ways[i][s][j] += ways[i][s - 1][j + 1]

        # Return total ways
        return ways

    def count_all_possible_ways(self, dimensions: int, steps: int, path_lengths: List[int],
                                nb_ways_grid: List[int]) -> int:
        c = {}
        # Count the possible ways for each individual dimension
        ways = self.count_ways(dimensions, steps, path_lengths)

        # Compute totals
        total = [ways[0][i][nb_ways_grid[0] - 1] for i in range(steps + 1)]

        for i in range(1, dimensions):
            for j in reversed(range(1, steps + 1)):
                k = j

                while k >= 0 and (j, k) not in c:
                    c[(j, k)] = self.choose(j, k)
                    k -= 1
                total[j] = sum(total[k] * c[(j, k)] * ways[i][j - k][nb_ways_grid[i] - 1] for k in range(j + 1))

        return total[steps] % self.MOD

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        T = int(input())

        for _ in range(T):
            n, m = map(int, input().split())
            x = list(map(int, input().split()))  # starting point
            grid = list(map(int, input().split()))  # dimensions

            print(self.count_all_possible_ways(n, m, grid, x))
