from typing import List


class CoinChange(object):
    """
    Source: Hackerrank / Algorithms / Dynamic Programming / The Coin Change Problem

    Input: amount n, and m coins

    Goal: find the nb of ways you can get to n using the given coins

    Idea: to get to value v using i coins = A[i - 1][v] + A[i][v - v_i] if v_i <= v
                                                                        else: = A[i - 1][v]
    """
    @staticmethod
    def nb_ways(n: int, m: int, coins: List[int]) -> int:
        result = [[1] for _ in range(m + 1)]
        for i in range(1, n + 1):
            result[0].append(0)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if coins[i - 1] <= j:
                    result[i].append(result[i - 1][j] + result[i][j - coins[i - 1]])
                else:
                    result[i].append(result[i - 1][j])
        return result[-1][-1]

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        n, m = map(int, input().split())
        coins = list(map(int, input().split()))
        print(self.nb_ways(n, m, coins))
