#source Hackerrank / Algorithms / Dynamic Programming / The Maximum Subarray

#input: unsorted array

#goal: compute max sum of uncontiguous and contiguous el in array

#idea: for case where all elements < 0, return the max of the array for both
#else, for the uncontiguous sum, return the sum of positive numbers

#for the contiguous sum, suppose we have the best sum so far, there are 2 cases:
#1) adding an element will keep our sum > 0, so we add it to the sum
#2) adding an element will make our sum < 0, so we start again from the next position with currSum = 0

def computeBestSum(a):
    unContiguSum = sum(filter(lambda x: x>0, a))
    if unContiguSum == 0:
        print max(a) , max(a)
    else:
        contiguSum = 0
        currSum = 0
        for x in a:
            currSum = max(0 , currSum + x)
            contiguSum = max(contiguSum , currSum)
        return contiguSum , unContiguSum

#Read input from Hackerrank
"""t = input()

for i in range(t):
    n = input()
    a = map(int , raw_input().split())
    computeBestSum(a)"""

#Custom Inputs
if __name__ == "__main__":
    print computeBestSum([1 , 2 , 3 , 4])
    print computeBestSum([2 , -1 , 2 , 3 , 4 , -5])
