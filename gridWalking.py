#source Hackerrank / Algorithms / Dynamic Programming / Grid Walking

#input: n dimensional grid , integer m

#goal: find the nb of ways you can take m steps without leaving grid. Each step can be taken
#forward or backward in any direction

#idea: to get to value v using i coins = A[i - 1][v] + A[i][v - v_i] if v_i <= v
#else: = A[i - 1][v]

import sys

MOD = 1000000007

def choose(n, k):
    if k < 0 or k > n:
        return 0
    else:
         p, q = 1, 1
         for i in range(1, min(k, n - k) + 1):
            p *= n
            q *= i
            n -= 1
         return p // q


def countWays(N, M, D):
    ways = [[[0] * D[i] for _ in range(M + 1)] for i in range(N)]
    # Find all possible ways for all points and steps
    #The first dimension is the number of dimensions n
    #The second dimension is the number of steps 1..M
    #The third dimension is the length of the path in this dimension

    for i in range(N): #ie for each dimension
        # Initial counting of zeroth and first steps
        for j in range(D[i]): #ie for each step we can take in this direction
            ways[i][0][j] = 1 #only 1 way if M = 0

            if j > 0:
                ways[i][1][j] += 1 # 2 ways if we're not on the edge
            if j < D[i] - 1:
                ways[i][1][j] += 1

        # Higher steps
        for s in range(2, M + 1):
            for j in range(D[i]): #for s > 1, then the #ways is sum of the number of ways to get to each neighbor with s-1 steps
                if j > 0:
                    ways[i][s][j] += ways[i][s - 1][j - 1]
                if j < D[i] - 1:
                    ways[i][s][j] += ways[i][s - 1][j + 1]

    # Return total ways
    return ways

def countAllPossibleWays(N , M , D , X):
    c = {}
    # Count the possible ways for each individual dimension
    ways = countWays(N , M , D)

    # Compute totals
    total = [ways[0][i][X[0] - 1] for i in range(M + 1)]

    for i in range(1, N):
        for j in reversed(range(1, M + 1)):
            k = j

            while k >= 0 and (j, k) not in c:
                c[(j, k)] = choose(j, k)
                k -= 1
            total[j] = sum(total[k] * c[(j, k)] * ways[i][j - k][X[i] - 1] for k in range(j + 1))

    return total[M] % MOD

#Read input from Hackerrank
"""T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, raw_input().split())
    X = map(int, raw_input().split()) #starting point
    grid = map(int, raw_input().split()) #dimensions

    print countAllPossibleWays(n , m , grid , X)"""

#Custom Inputs
if __name__ == '__main__':
    n = 2
    m = 3
    X = [1 , 1]
    grid = [2 , 3]
    print countAllPossibleWays(n , m , grid , X)
