#source Hackerrank / Algorithms / Dynamic Programming / Red John is Back

#input: t integers n representing the width of the wall

#goal: compute the # of ways you can put 4x1 and 1x4 bricks in this wall = m
#Then output the # of prime numbers smaller than m

#idea: if you get from i-1 to i:
#case 1: i <= 3: return 1
#case 2: i = 4: return 2
#case 3: i > 4: return A[i - 1] + A[i - 4]
#for each step of the iteration, if the result is prime, output += 1

import math
def isPrime(n):
    if n < 2 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def getNbPrimes(n):
    result = 0
    for i in range(n + 1):
        if isPrime(i):
            result += 1
    return result

def solveRedJohnIsBack(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1
    else:
        A = [0 , 1 , 1 , 1 , 2]
        for i in range(5 , n + 1):
            A.append(A[-1] + A[-4])
        return getNbPrimes(A[-1])

#Read input from Hackerrank
"""t = input()
for i in range(t):
    print solveRedJohnIsBack(input())
"""

#Custom Inputs
if __name__ == "__main__":
    print solveRedJohnIsBack(1)
    print solveRedJohnIsBack(7)
