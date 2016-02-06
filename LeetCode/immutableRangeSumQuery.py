#input : array of integers

#goal: Be able to compute the most efficiently possible the sum in a given range
#Indeed a lot of calls will be made to the sumRange function

#idea: Store for every index the sum from all the way to the left until this index

#complexity: O(n) in time to store the sums and then constant lookup for each call to sumRange and O(n) in space

class immutableRangeSum:
    def __init__(self , ar):
        self.leftSums = [0 for _ in range(len(ar))]
        self.leftSums[0] = ar[0]
        for i in range(1 , len(ar)):
            self.leftSums[i] = self.leftSums[i - 1] + ar[i]

    def sumRange(self , i , j):
        if i <= 0:
            return self.leftSums[j]
        else:
            return self.leftSums[j] - self.leftSums[i - 1]

nums = [-2, 0, 3, -5, 2, -1]
imm = immutableRangeSum(nums)
print imm.sumRange(0, 2) , "should be" , 1
print imm.sumRange(2, 5) , "should be" , -1
print imm.sumRange(0, 5) , "should be" , -3
