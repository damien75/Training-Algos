import math

class RedJohnIsBack(object):
    """
    Source Hackerrank / Algorithms / Dynamic Programming / Red John is Back

    Input: t integers n representing the width of the wall

    Goal: compute the # of ways you can put 4x1 and 1x4 bricks in this wall = m
    Then output the # of prime numbers smaller than m

    Idea: if you get from i-1 to i:
    case 1: i <= 3: return 1
    case 2: i = 4: return 2
    case 3: i > 4: return A[i - 1] + A[i - 4]
    for each step of the iteration, if the result is prime, output += 1
    """
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

    def count_primes(self, n: int) -> int:
        result = 0
        for i in range(n + 1):
            if self.is_prime(i):
                result += 1
        return result

    def solve_red_john_is_back(self, n: int) -> int:
        if n < 4:
            return 0
        elif n == 4:
            return 1
        else:
            ar = [0 , 1 , 1 , 1 , 2]
            for i in range(5 , n + 1):
                ar.append(ar[-1] + ar[-4])
            return self.count_primes(ar[-1])

    def read_and_print_from_hackerrank(self):
        """
        Utility function to read from hackerrank stdin and return to stdout
        """
        t = int(input())
        for i in range(t):
            print(self.solve_red_john_is_back(int(input())))
