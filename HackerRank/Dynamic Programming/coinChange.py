#source Hackerrank / Algorithms / Dynamic Programming / The Coin Change Problem

#input: amount n, and m coins

#goal: find the nb of ways you can get to n using the given coins

#idea: to get to value v using i coins = A[i - 1][v] + A[i][v - v_i] if v_i <= v
#else: = A[i - 1][v]

def nbWays(n , m , coins):
    A = [[1] for _ in range(m + 1)]
    for i in range(1 , n + 1):
        A[0].append(0)

    for i in range(1 , m + 1):
        for j in range(1 , n + 1):
            if coins[i - 1] <= j:
                A[i].append(A[i - 1][j] + A[i][j - coins[i - 1]])
            else:
                A[i].append(A[i - 1][j])
    return A[-1][-1]

#Read input from Hackerrank
"""n , m = map(int , raw_input().split())
coins = map(int , raw_input().split())
print nbWays(n , m , coins)
"""

#Custom Inputs
if __name__ == "__main__":
    print nbWays(4 , 3 ,[1 , 2 , 3])
    print nbWays(10 , 4 ,[2 , 5 , 3 , 6])
