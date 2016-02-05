#input : array of stock prices

#goal: Find the sequence of buy, sell and cooldown to maximize profit
#In this case you can have only 1 stock, when bought you can only sell it and not buy more

#idea: Dynamic Programming
#go from left to right through the prices
#for each index i, check what happens if you buy or sell at this moment
#   buy[i] = max(buy[i - 1] , -prices[i] if i < 2 else sell[i - 2] - prices[i])
#Here first case is we bought cheaper before, and keep track of our portfolio, second is when we sold and have cooled down, we buy again
#   sell[i] = max(sell[i - 1] , buy[i - 1] + prices[i])
#Here first case is we are cooling down, second is we are actually selling and store our current profit

#complexity: O(n) in time and O(n) in space

def maxProfit(prices):
    buy0 = buy1 = -prices[0]
    sell0 = sell1 = sell2 = 0
    for i in range(1 , len(prices)):
        buy0 = max(buy0 , sell2 - prices[i])
        sell0 = max(sell1 , buy1 + prices[i])
        sell2 = sell1
        sell1 = sell0
        buy1 = buy0
    return sell0

#Example:

prices = [1, 2, 3, 0, 2]
#transactions = [buy, sell, cooldown, buy, sell]
print maxProfit(prices) , "should be equal to" , 3
