#source Hackerrank / Algorithms / Dynamic Programming / The Longest Increasing Subsequence

#input: sequence of integers of size n

#goal: find the length of the longest subsequence of increasing integers in this array

#idea: solution in O(n log n) time complexity
#go through the array in normal path, from left to right
#when we see a new element a[i]:
#a[i] is smaller than all other last elements of the list we have so far => create new list of size 1 with a[i] as last element and remove other list of size 1
#a[i] is bigger than all others => add it to the list of longest length so far
#a[i] is between smallest and biggest => add it to the list where its end element is smallest and it's bigger than a[i] and remove all lists of same length

def findPosition(ar , el):
    left = -1
    right = len(ar) - 1
    while right > left + 1:
        m = (left + right)/2
        if ar[m] >= el:
            right = m
        else:
            left = m
    return right

def lengthOfLongestSubSequence(a):
    if len(a) == 0:
        return
    else:
        lastElement = [a[0]]
        bestLength = 1
        for i in range(1 , len(a)):
            if a[i] < lastElement[0]:
                lastElement[0] = a[i]
            elif a[i] > lastElement[bestLength - 1]:
                bestLength += 1
                lastElement.append(a[i])
            else:
                lastElement[findPosition(lastElement , a[i])] = a[i]
        return bestLength

#Read input from Hackerrank
"""n = input()
a = [0]*n
for i in range(n):
    a[i] = input()
print lengthOfLongestSubSequence(a)
"""

#Custom Inputs
if __name__ == "__main__":
    n = 10
    a = [29471, 5242, 21175, 28931, 2889, 7275, 19159, 21773, 1325, 6901]
    print lengthOfLongestSubSequence(a) == 4
    a = [2 , 7 , 4 , 3 , 8]
    print lengthOfLongestSubSequence(a) == 3
