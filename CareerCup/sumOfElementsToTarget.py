#The 2010 Census puts populations of 26 largest US metro areas at
population = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]

#Can you find a subset of these areas where a total of exactly 100,000,000 people live,
#assuming the census estimates are exactly right? Provide the answer and code or reasoning used.

#input: array of numbers

#goal: add these numbers to get to a given value

#idea: DP
#have an array A that tells us for A[i,j] if we can have a subset of city_0..city_i that sums up to j
#we initialize it with A[0 , j] = (False , [])
#A[i , 0] = (True , [])
#for i in range(1 , n):
#   for j in range(target):
#      if city_i == j or A[i - 1][j][0] or (j - city_i >=0 and A[i - 1][j - city_i][0]):
#         A[i][j] = (True , A[i - 1][j][1] or A[i - 1][j - city_i][1] + [city_i])

#A = [{population[i] : [i] for i in range(n)}]
#for i in range(1 , n):
#   A.append({})
#   for j in range(target):
#      if j in A[0] or j in A[i - 1]:
#         A[i][j] = A[0][j] or A[i - 1][j]
#      for city in A[0]:
#         if j - city in A[i - 1]:
#            A[i][j] = A[i - 1][j - city] + city

#BOTH TOO LONG BECAUSE TARGET TO BIG AND COMPLEXITY EXPONENTIAL IN TARGET!! --> DIVIDE AND CONQUER

target = 100000000
print population

import time

class subsetToTarget:
    def __init__(self , data):
        self.data = sorted(data)

    def solveWithStack(self , fromIndex , stack , stackIndex , target):
        found = False
        if target == 0:
            #we have found our subset to reach the target! SUCCESS
            print stack[:stackIndex]
            found = True
            return found
        while (fromIndex < len(self.data) and self.data[fromIndex] > target):
            fromIndex += 1
        while (fromIndex < len(self.data) and self.data[fromIndex] <= target):
            stack[stackIndex] = self.data[fromIndex]
            found = self.solveWithStack(fromIndex + 1 , stack , stackIndex + 1 , target - self.data[fromIndex])
            if found:
                return found
            fromIndex += 1
        return found

start = time.time()
s = subsetToTarget(population)
s.solveWithStack(0 , [0]*len(s.data) , 0 , target)
print "solution found in" , time.time() - start
