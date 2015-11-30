#source Hackerrank / Algorithms / Dynamic Programming / Knapsack

#input: max capacity W, and int values

#goal: compute the max sum not exceeding W using only elements in the given list

#idea: when W = 0 => expected value = 0
#when len(values) = 0 => expected value = 0
#for cap w and first i values:
#   if values[i] <= cap:
#       expectedValue = max(expectedValue[i - 1][cap] , expectedValue[i][cap - values[i]] + values[i])

class Knapsack:
    def __init__(self , values , maxCapacity):
        self.A = []
        self.values = values
        self.W = maxCapacity

    def getExpectedValue(self):
        for i in range(len(self.values) + 1):        #add 0 when capacity is equal to 0
            self.A.append([0])
        for i in range(1 , self.W + 1):              #add 0 when there are no available values
            self.A[0].append(0)

        for i in range(1 , len(self.values) + 1):
            j = i - 1
            for cap in range(1 , self.W + 1):
                if self.values[j] > cap:
                    self.A[i].append(self.A[i - 1][cap])
                else:
                    self.A[i].append(max(self.A[i - 1][cap] , self.A[i][cap - self.values[j]] + self.values[j]))
        return self.A[-1][-1]


#Read input from Hackerrank
"""t = input()

for _ in range(t):
    n , W = map(int , raw_input().split())
    values = map(int , raw_input().split())
    knap = Knapsack(values , W)
    print knap.getExpectedValue()
"""

#Custom Inputs
if __name__ == "__main__":
    W = 12
    values = [1 , 6 , 9]
    knap = Knapsack(values , W)
    print knap.getExpectedValue()
    W = 9
    values = [3 , 4 , 4 , 4 , 8]
    knap = Knapsack(values , W)
    print knap.getExpectedValue()
