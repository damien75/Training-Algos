#source Hackerrank / Algorithms / Dynamic Programming / The Coin Change Problem

#input: evolution of a stock in time (1 <= time <= n) for t test cases

#goal: compute the max profit we can make, we can either buy 1 share every time or sell all we have

#idea: go in time from right to left
#m = 0 price at which we will sell the shares
#if the price[i] >= m then m = price[i] #in this case we will sell the preceding shares at this price, so we reset m
#profit += m - price[i]

def maximizeStock(n , price):
    profit = 0
    m = 0
    for j in range(n - 1 , -1 , -1):
        if price[j] >= m:
            m = price[j]
        else:
            profit += m - price[j]
    return profit


#Read input from Hackerrank
"""t = input()
for i in range(t):
    n = input()
    price = map(int , raw_input().split())
    print maximizeStock(n , price)
"""

#Custom Inputs
if __name__ == "__main__":
    print maximizeStock(3 , [5 , 3 , 2])
    print maximizeStock(3 , [1 , 2 , 100])
    print maximizeStock(4 , [1 , 3 , 1 , 2])
