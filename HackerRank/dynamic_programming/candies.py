#source Hackerrank / Algorithms / Dynamic Programming / Candies

#input: n ratings for children in class

#goal: min nb of candies to buy so that at least each student has 1 candy, and a child with a better grade
#than his neighbor gets more candies

#idea: start with 1 candy, and store the grade
#As we move on, if the grade is bigger, then increase the nb of candies to give
#               else put it back to 1
#do this from left to right and right to left, and then get the max of both

def minNbCandies(n , rating):
    left = [1 for _ in range(n)]
    right = [1 for _ in range(n)]

    leftGrade = rating[0]
    rightGrade = rating[-1]

    for i in range(1 , n):
        j = n - i - 1
        if rating[i] > leftGrade:
            left[i] = left[i - 1] + 1
        leftGrade = rating[i]
        if rating[j] > rightGrade:
            right[j] = right[j + 1] + 1
        rightGrade = rating[j]

    return sum(max(left[i] , right[i]) for i in range(n))

#Read input from Hackerrank
"""n = input()
rating = []
for i in range(n):
    rating.append(input())
print nbWays(n , m , coins)
"""

#Custom Inputs
if __name__ == "__main__":
    print minNbCandies(3 , [1 , 2 , 2])
