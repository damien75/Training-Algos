from heapq import heappop, heappush
from typing import List


class SnakesAndLadders(object):
    """
    Source Hackerrank / Algorithms / Search / Snakes And Ladders

    Input: array of shortcuts (ladders to go up faster and snakes to go back down)

    Goal: find fastest way to get to the top, where we can roll a dice every time

    Idea: store jumps in array, if no snake or ladder at this position then jumps[i] = i
    then use a heap sorted using the number of tosses used to get there
    keep track of the positions already explored and stop when we've reached the top or run out of tries
    """

    @staticmethod
    def min_number_of_toss(jumps: List[int], top: int) -> int:
        positions = [(0, 1)]
        explored = [False for _ in range(top + 7)]

        while len(positions) > 0:
            nb_toss, p = heappop(positions)
            while explored[p]:
                if len(positions) <= 0:
                    return -1
                nb_toss, p = heappop(positions)
            explored[p] = True
            if p == top:
                return nb_toss
            elif p < top:
                for i in range(1, 7):
                    heappush(positions, (nb_toss + 1, jumps[p + i]))
        return -1

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())
        top = 100
        for _ in range(t):
            n = int(input())
            jumps = [i for i in range(top + 8)]
            for _ in range(n):
                s, e = map(int, input().split())
                jumps[s] = e
            m = int(input())
            for _ in range(m):
                s, e = map(int, input().split())
                jumps[s] = e
            print(self.min_number_of_toss(jumps, top))
