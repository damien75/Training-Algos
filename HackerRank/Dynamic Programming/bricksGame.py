#source Hackerrank / Algorithms / Dynamic Programming / Bricks Game

#input: stack of integers size n

#goal: maximize nb of collected integers in a one to one game where each player can take 1,2 or 3 numbers every time

#idea: go through array from right to left
#store the backwards sum and the max score we can get if we start at a given position
#when we get to position i, we have 3 cases:
#1. if we take only 1 brick then our score is bricks[i] + reversedSum[i + 1] - maxScore[i + 1]
#2. if we take 2 bricks then our score is bricks[i] + bricks[i + 1] + reversedSum[i + 2] - maxScore[i + 2]
#3. if we take 3 bricks then our score is bricks[i] + bricks[i + 1] + bricks[i + 2] + reversedSum[i + 3] - maxScore[i + 3]

#In the end we just get the max score we can have from position 0

def maxScore(n , bricks):
    if n <= 3:
        return sum(bricks)
    else:
        maxScore = [0] * n
        maxScore[-1] = bricks[-1]
        maxScore[-2] = maxScore[-1] + bricks[-2]
        maxScore[-3] = maxScore[-2] + bricks[-3]

        reversedSum = maxScore[:]  #THIS IS THE BEST WAY TO DO AN ELEMENT BY ELEMENT COPY AND NOT ADDRESS COPY
        for i in range(n - 4, -1, -1):
            case1 = bricks[i] + reversedSum[i + 1] - maxScore[i + 1]
            case2 = bricks[i] + bricks[i + 1] + reversedSum[i + 2] - maxScore[i + 2]
            case3 = bricks[i] + bricks[i + 1] + bricks[i + 2] + reversedSum[i + 3] - maxScore[i + 3]

            maxScore[i] = max(case1, case2, case3)
            reversedSum[i] = reversedSum[i + 1] + bricks[i]

        return maxScore[0]

#Read input from Hackerrank
"""t = input()

for _ in range(t):
    n = input()
    bricks = map(int, raw_input().split())
    print maxScore(n , bricks)
"""

#Custom Inputs
if __name__ == "__main__":
    n = 5
    bricks = [999 , 1 , 1 , 1 , 0]
    print maxScore(n , bricks)
    bricks = [0 , 1 , 1 , 1 , 999]
    print maxScore(n , bricks)
