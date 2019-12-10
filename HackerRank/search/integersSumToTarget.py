#input: integer array

#goal: output all sets of 3 values that sum up to target t, ie n1 + n2 + n3 = t

#idea: complexity O(n^2)
#1st: sort the array
#for each element in the array:
#   tempTarget = t - currElement
#   have 2 pointers left and right with left initially = currPos + 1 and right len(ar) - 1
#   while left < right:
#       tempSum = left + right
#       if sum < tempTarget:
#           left += 1
#       elif sum > tempTarget:
#           right -= 1
#       else:
#           results.append((currElement , left , right))

def getSetsOfThreeThatSumToTarget(ar , t):
    ar.sort()
    results = []
    for i in range(len(ar) - 2):
        tempTarget = t - ar[i]
        left = i + 1
        right = len(ar) - 1
        while left < right:
            tempSum = ar[left] + ar[right]
            if tempSum < tempTarget:
                left += 1
            elif tempSum > tempTarget:
                right -= 1
            else:
                results.append((ar[i] , ar[left] , ar[right]))
                left += 1
                right -= 1
    return results

#goal: output all sets of 2 values that sum up to target t, ie n1 + n2 = t

#idea: complexity O(n)
#for each element in the array:
#   store the element in a set (or hashtable)
#for each element in the array:
#   look up if t - element is in the hashtable
#   if so:
#       results.append((element , t - element))

def getSetsOfTwoThatSumToTarget(ar , t):
    s = set()
    results = []
    for el in ar:
        s.add(el)
    for el in ar:
        if t - el in s:
            results.append((el , t - el))
    return results

print getSetsOfThreeThatSumToTarget([2, 3, 1, -2, -1, 0, 2, -3, 0] , 0)
print getSetsOfTwoThatSumToTarget([2, 3, 1, -2, -1, 0, 2, -3, 0] , 2)
