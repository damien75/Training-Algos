from typing import List


class MinimumNumberOfCandies(object):
    """
    Source: Hackerrank / Algorithms / Dynamic Programming / Candies

    Input: n ratings for children in class

    Goal: min nb of candies to buy so that at least each student has 1 candy, and a child with a better grade
    than his neighbor gets more candies

    Idea: start with 1 candy, and store the grade
    As we move on, if the grade is bigger, then increase the nb of candies to give
                   else put it back to 1
    do this from left to right and right to left, and then get the max of both
    """
    @staticmethod
    def min_nb_candies(n: int, rating: List[int]) -> int:
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]

        left_grade = rating[0]
        right_grade = rating[-1]

        for i in range(1 , n):
            j = n - i - 1
            if rating[i] > left_grade:
                left[i] = left[i - 1] + 1
            left_grade = rating[i]
            if rating[j] > right_grade:
                right[j] = right[j + 1] + 1
            right_grade = rating[j]

        return sum(max(left[i] , right[i]) for i in range(n))

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        n = int(input())
        rating = []
        for i in range(n):
            rating.append(int(input()))
        print(self.min_nb_candies(n, rating))
