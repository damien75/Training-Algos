#input : integer array ar and integer k

#goal: Find the maximum length of a subarray that sums to k.
#If there isn't one, return 0

#idea: Use a hashtable with key: the sum from start to the current index and value: current index
#Then we do a single scan, left to right
#for i in range(len(ar)):
#   tempSum += ar[i]
#   if tempSum not in hashtable:
#       hashtable[tempSum] = i
#   if tempSum - k in hashtable: <-- in that case the sum from this index to the current index is k!!
#       maxLength = max(maxLength , i - hashtable[tempSum - k])

#complexity: 0(n) single scan in time and 0(n) in space

def maxLengthSubArrayToTarget(ar , target):
    tempSum = 0
    maxLength = 0
    h = {0 : -1}
    for i in range(len(ar)):
        tempSum += ar[i]
        if tempSum not in h:
            h[tempSum] = i
        if tempSum - target in h:
            maxLength = max(maxLength , i - h[tempSum - target])
    return maxLength

#Example 1:
ar1 = [1, -1, 5, -2, 3]
k1 = 3
print maxLengthSubArrayToTarget(ar1 , k1)
#expect to return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

#Example 2:
ar2 = [-2, -1, 2, 1]
k2 = 1
#expect to return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
print maxLengthSubArrayToTarget(ar2 , k2)
