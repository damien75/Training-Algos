from typing import List


class MaxScore(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / Bricks Game

    Input: stack of integers size n

    Goal: maximize nb of collected integers in a one to one game where each player can take 1,2 or 3 numbers every time

    Idea: go through array from right to left
    store the backwards sum and the max score we can get if we start at a given position
    when we get to position i, we have 3 cases:
    1. if we take only 1 brick then our score is bricks[i] + reversedSum[i + 1] - maxScore[i + 1]
    2. if we take 2 bricks then our score is bricks[i] + bricks[i + 1] + reversedSum[i + 2] - maxScore[i + 2]
    3. if we take 3 bricks then our score is bricks[i] + bricks[i + 1] + bricks[i + 2] + reversedSum[i + 3] - maxScore[i + 3]

    In the end we just get the max score we can have from position 0
    """
    @staticmethod
    def max_score(n: int, bricks: List[int]) -> int:
        if n <= 3:
            return sum(bricks)
        else:
            max_score = [0] * n
            max_score[-1] = bricks[-1]
            max_score[-2] = max_score[-1] + bricks[-2]
            max_score[-3] = max_score[-2] + bricks[-3]

            reversed_sum = max_score[:]  # THIS IS THE BEST WAY TO DO AN ELEMENT BY ELEMENT COPY AND NOT ADDRESS COPY
            for i in range(n - 4, -1, -1):
                case1 = bricks[i] + reversed_sum[i + 1] - max_score[i + 1]
                case2 = bricks[i] + bricks[i + 1] + reversed_sum[i + 2] - max_score[i + 2]
                case3 = bricks[i] + bricks[i + 1] + bricks[i + 2] + reversed_sum[i + 3] - max_score[i + 3]

                max_score[i] = max(case1, case2, case3)
                reversed_sum[i] = reversed_sum[i + 1] + bricks[i]

            return max_score[0]

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())

        for _ in range(t):
            n_read = int(input())
            bricks_read = list(map(int, input().split()))
            print()
            print(self.max_score(n_read, bricks_read))
